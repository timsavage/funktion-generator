#ifndef _BOOT__H
#define _BOOT__H

#include <TFT_ILI9163C.h>

#define INIT_SYSTEM(message) boot_message(message)
#define INIT_SUBSYSTEM(message) boot_message(message, LIGHT_GREY, '-')
#define INIT_INFO(message) boot_message(message, CYAN, '?')
#define INIT_ERROR(message) boot_message(message, RED, '!')
#define INIT_HALT(message) boot_message(message, RED, '!'); while(1) { delay(1000); }
#define INIT_OK(value) tft.setTextColor(GREEN); tft.print(value); Serial.print(value)
#define INIT_PRINT(value) tft.print(value); Serial.print(value)

/**
 * Initialise boot (eg supply TFT interface)
 */
void start_boot(TFT_ILI9163C* display);

#endif //!_BOOT_H

