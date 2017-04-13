#include "ui.h"
#include "wave_tables.h"


typedef struct MenuItem {
  uint8_t id;
  char title[32];
} MenuItem;


/**
 * Render a waveWidget
 */
void ui_waveWidget_render(TFT_ILI9163C* tft, WaveTable* wt, int16_t x, int16_t y) {
  uint16_t color = tft->Color565(16, 32, 16);
  tft->fillRect(x, y, 68, 68, BLUE);
  tft->fillRoundRect(x, y, 68, 68, 10, color);

  x += 2;
  y += 2;

  const uint8_t scale = 2;
  const uint8_t size = WAVE_TABLE_MAX >> 2;
  const uint8_t step = 1 << scale;
  const uint8_t offset = y + size;
  uint8_t sidx, idx;

  color = tft->Color565(0, 64, 0);
  for (idx = 8; idx < 64; idx += 8) {
    tft->drawLine(x+idx, y, x+idx, y+64, color);
    tft->drawLine(x, y+idx, x+64, y+idx, color);
  }
  
  for (idx = 0; idx < size; idx++) {
    sidx = idx << scale;
    tft->drawLine(
      x + idx, offset - (wt->data[sidx] >> scale),
      x + idx + 1, offset - (wt->data[sidx + step] >> scale),
      GREEN
    );
  }
}

/**
 * Render a menu
 */
void ui_menuMenu_render(TFT_ILI9163C* tft) {
  
}

void ui_mainScreenFreq(TFT_ILI9163C* tft, uint32_t frequency=1234567) {
  tft->setTextColor(YELLOW);
  tft->setTextScale(2);
  tft->setCursor(10, 25);

  if (frequency >= 10000) {
    tft->print(frequency/1000.0); tft->setTextScale(1); tft->print("kHz");
  } else if (frequency >= 10000000) {
    tft->print(frequency/1000000.0); tft->setTextScale(1); tft->print("mHz");
  } else {
    tft->print(frequency); tft->setTextScale(1); tft->print("Hz");
  }
}

void ui_mainScreen(TFT_ILI9163C* tft) {
  tft->fillCircle(16, 16, 16, BLUE);
  tft->fillCircle(tft->width()-9, 8, 8, BLUE);
  tft->fillRect(16, 0, tft->width() - 24, 17, BLUE);
  tft->drawLine(0, 16, 0, tft->height(), BLUE);
  tft->fillRoundRect(1, 17, 64, 22, 10, BLACK);

  tft->setTextColor(WHITE);
  tft->setCursor(16, 6);
  tft->print("Funktion Gen");

  ui_mainScreenFreq(tft);

  WaveTable wt = WaveTable();
  if (wt_load(&wt, "/Sine.wave") == WAVE_FILE_OK) {
    ui_waveWidget_render(tft, &wt, tft->width() - 69, tft->height() - 69);
  }
}

extern void ui_update(TFT_ILI9163C* tft) {
  ui_mainScreen(tft);
}

