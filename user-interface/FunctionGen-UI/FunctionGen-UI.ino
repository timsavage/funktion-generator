#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <FS.h>
#include <SPI.h>
#include <TFT_ILI9163C.h>
#include <Wire.h>

#include "wave_tables.h"
#include "ui.h"

#define __TFT_CS  D0  //(D0)
#define __TFT_DC  D8   //(D1)



const char* mdnsName = "FunktionGen";


TFT_ILI9163C tft = TFT_ILI9163C(__TFT_CS, __TFT_DC);
WiFiUDP server = WiFiUDP();
WaveTable currentWave = WaveTable();

uint32_t currentFrequency = 1000; // 1kHz


/**
 * Draw a wave table
 * 
 * @param waveTable - A pointer to a 256 byte wavetable.
 * @param scale - Scale the size of the table by a power of 2 (uses binary shift).
 * @param x - X offset of table.
 * @param y - Y Offset of table.
 * @param color - Colour too render table with.
 */
void drawWave(TFT_ILI9163C* display, const WaveTable* waveTable, uint8_t scale=0, uint8_t x=0, uint8_t y=0, uint16_t color=YELLOW) {
  const uint8_t size = WAVE_TABLE_MAX >> scale;
  const uint8_t step = 1 << scale;
  const uint8_t offset = y + size;
  uint8_t sidx;
  for (uint8_t idx = 0; idx < size; idx++) {
    sidx = idx << scale;
    display->drawLine(
      x + idx, offset - (waveTable->data[sidx] >> scale),
      x + idx + 1, offset - (waveTable->data[sidx + step] >> scale),
      color
    );
  }
}


void init_message(const char* message, uint16_t color=WHITE, const char icon='+') {
  tft.setTextColor(color);
  tft.print("["); tft.print(icon); tft.print("] "); tft.print(message);
  Serial.print("["); Serial.print(icon); Serial.print("] "); Serial.print(message);
}

#define INIT_SYSTEM(message) init_message(message)
#define INIT_SUBSYSTEM(message) init_message(message, LIGHT_GREY, '-')
#define INIT_INFO(message) init_message(message, CYAN, '?')
#define INIT_ERROR(message) init_message(message, RED, '!')
#define INIT_HALT(message) init_message(message, RED, '!'); while(1) { delay(1000); }
#define INIT_OK(value) tft.setTextColor(GREEN); tft.print(value); Serial.print(value)
#define INIT_PRINT(value) tft.print(value); Serial.print(value)


/**
 * Initilise network
 * 
 * @param connect_timeout - Timeout for wifi connection (in seconds)
 */
void init_network(uint16_t port=10001, uint8_t connect_timeout=20) {
  INIT_SYSTEM("Init Network\n");

  // Wifi
  INIT_SUBSYSTEM("Joining SSID: "); INIT_PRINT(ssid); INIT_PRINT('\n');
  WiFi.begin(ssid, password);

  INIT_SUBSYSTEM("Connecting ");
  connect_timeout = connect_timeout * 4; // Loop is ~1/4 second
  while (WiFi.status() != WL_CONNECTED) {
    if (connect_timeout-- == 0) {
      INIT_ERROR("\nConnect timeout\n");
      return;
    }
    delay(250); 
    INIT_PRINT(".");
  }
  INIT_PRINT('\n'); INIT_INFO("IP address: "); INIT_PRINT(WiFi.localIP()); INIT_PRINT('\n');

  // Zeroconf
  INIT_SYSTEM("Starting mDNS service\n");
  INIT_SUBSYSTEM("Listening on: "); INIT_PRINT(mdnsName); INIT_PRINT('\n'); 
  if (!MDNS.begin(mdnsName)) {
    INIT_ERROR("Unable to start mDNS service\n");
    return;
  }

  INIT_SYSTEM("Start UDP server\n");
  if (!server.begin(port)) {
    INIT_ERROR("Unable to start UDP server\n");
    return;
  }

  INIT_SUBSYSTEM("Publish mDNS service\n");
  MDNS.addService("wave", "udp", port);
}

/**
 * Initialise
 */
void initialise() {
  // Initilaise tft first.
  tft.begin();

  // Initialise File system
  INIT_SYSTEM("Init FS\n");
  SPIFFS.begin();
  FSInfo fs_info;
  if (SPIFFS.info(fs_info)) {
    INIT_INFO("Total: "); INIT_PRINT(fs_info.totalBytes / 1024); INIT_PRINT("kB\n");
    INIT_INFO("Total: "); INIT_PRINT(fs_info.usedBytes / 1024); INIT_PRINT("kB\n");
  } else {
    INIT_HALT("Failed initilising filesystem.");
  }

  // Init TWI
  INIT_SYSTEM("Init TWI\n");
  Wire.begin();
 
  // Init DDS Generator
  INIT_SYSTEM("Init DDS Generator\n");

  // Init network
  init_network();

  // Complete
  INIT_OK("Init complete.");  
}


void setup() {
  Serial.begin(115200);
  
  initialise();
  delay(500);
  
  tft.clearScreen();
  ui_update(&tft);
}


char packetBuffer[0xFF];

void loop(void) {
  size_t packetSize = server.parsePacket();
  if (packetSize) {
    // Process UDP packet.
    size_t len = server.read(packetBuffer, 0xFF);
    if (len > 0) {
      Serial.print("Received: "); Serial.println(packetBuffer);
    }
  }
}


