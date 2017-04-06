#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <FS.h>
#include <SPI.h>
#include <TFT_ILI9163C.h>
#include <Wire.h>

#include "wave_tables.h"

// Color definitions
#define BLACK    0x0000
#define BLUE     0x001F
#define RED      0xF800
#define GREEN    0x07E0
#define CYAN     0x07FF
#define MAGENTA  0xF81F
#define YELLOW   0xFFE0 
#define WHITE    0xFFFF

#define __TFT_CS  D0  //(D0)
#define __TFT_DC  D8   //(D1)


const char* ssid = "Penguins!";
const char* password = "";
const char* mdnsName = "FunktionGen";


TFT_ILI9163C tft = TFT_ILI9163C(__TFT_CS, __TFT_DC);
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

void init_halt(const char* message) {
    tft.setTextColor(RED);
    tft.print("[!] Halt: "); tft.println(message);
    while(1) { delay(1000); }
}

void init_network() {
  tft.println("[+] Init Network");
  
  tft.print("[-] Joining SSID: "); tft.println(ssid);
  WiFi.begin(ssid, password);
  
  tft.print("[-] Connecting ");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500); tft.print(".");
  }
  tft.println("");

  tft.print("[-] IP address: "); tft.println(WiFi.localIP());


  tft.println("[+] Starting MDNS");
  
  tft.print("[-] Listening on: "); tft.println(mdnsName);  
  if (!MDNS.begin(mdnsName)) {
    init_halt("Error setting up MDNS responder!");
  }
  tft.println("[-] Adding service: wave");
  MDNS.addService("wave", "tcp", 10001);
}

void initialise() {
  // Initilaise tft first.
  tft.begin();
  tft.setTextColor(WHITE);

  // Initialise File system
  tft.println("[+] Init FS");
  SPIFFS.begin();
  FSInfo fs_info;
  if (SPIFFS.info(fs_info)) {
    tft.print("[-] Total Bytes: "); tft.println(fs_info.totalBytes);
    tft.print("[-] Used Bytes: "); tft.println(fs_info.usedBytes);
  } else {
    tft.setTextColor(RED);
    tft.print("[!] Failed");
    tft.setTextColor(WHITE);
  }

  // Init TWI
  tft.println("[+] Init TWI");
  Wire.begin();

  // Init network
  init_network();
  
  // Init DDS Generator
  tft.println("[+] Init DDS Generator");
}

void setup() {
  initialise();

  tft.setTextColor(YELLOW);
  Dir dir = SPIFFS.openDir("/");
  while (dir.next()) {
    String fileName = dir.fileName();
    if (fileName.endsWith(".wave")) {
      tft.print(fileName); tft.print(" (");
      File f = dir.openFile("r");
      tft.print(f.size()); tft.println("b)");
    }
  }

  WaveTable wave;
  
  wt_zero(&wave);
  uint8_t result = wt_load(&wave, "/Random.wave");
  if (result != WAVE_FILE_OK) {
    tft.setTextColor(RED);
    tft.print("Error reading wave: "); tft.println(wt_errorMessage(result));
    return;
  } else {
    tft.setTextColor(GREEN);
    tft.print("Read wave: "); tft.println(wave.name);
  }
  
  drawWave(&tft, &wave, 1, 0, 0, CYAN);
  wt_mirror(&wave);
  drawWave(&tft, &wave, 1, 0, 0, MAGENTA);
  wt_invert(&wave);
  drawWave(&tft, &wave, 1, 0, 0, BLUE);
}

void loop(void) {
  
}


