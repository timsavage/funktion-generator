#include <SPI.h>
#include <Wire.h>
#include <TFT_ILI9163C.h>

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

void setup() {
  tft.begin();

  WaveTable wave;
  tft.setTextColor(GREEN);
  tft.setTextScale(2);
  for (uint8_t i = WAVE_SINE; i < WAVE_RSAWTOOTH; i++) {
    loadBuiltinWave(&wave, i);
    drawWave(&tft, &wave, 3, 0, (i - 1) * 32);
    tft.setCursor(34, (i - 1) * 32);
    tft.print(wave.name);
  }
}

void loop(void) {
  
}


