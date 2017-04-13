#include "boot.h"

TFT_ILI9163C* pDisplay = NULL;

extern void boot_begin(TFT_ILI9163C* display) {
  pDisplay = display;
}

extern void boot_message(const char* message, uint16_t color, const char icon) {
  pDisplay->setTextColor(color);
  if (icon == NULL) {
    pDisplay->print(message);
    Serial.print(message);
  } else {
    pDisplay->print("["); pDisplay->print(icon); pDisplay->print("] "); pDisplay->print(message);
    Serial.print("["); Serial.print(icon); Serial.print("] "); Serial.print(message);
  }
}

