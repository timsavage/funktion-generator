/**
 * wave_tables.h
 * 
 * Definition of wave table structure and data tables.
 * 
 */
#ifndef _WAVE_TABLES__H
#define _WAVE_TABLES__H

#include <stdint.h>

// Wave table constants
const size_t WAVE_NAME_LEN = 17; // 16 Chars
const size_t WAVE_TABLE_MAX = 0xFF;
const size_t WAVE_TABLE_LEN = WAVE_TABLE_MAX + 1;
const uint8_t WAVE_DYNAMIC_RANGE = 0xFF;

// Result code defines
#define WAVE_FILE_OK                   0
#define WAVE_FILE_NOT_FOUND            1
#define WAVE_FILE_INVALID_HEADER       2
#define WAVE_FILE_UNKNOWN_VERSION      3
#define WAVE_FILE_CHECKSUM_FAILED      4
#define WAVE_FILE_ERROR_WRITING_HEADER 5
#define WAVE_FILE_ERROR_WRITING_DATA   6
#define WAVE_FILE_MAX_ERROR WAVE_FILE_ERROR_WRITING_DATA


/**
 * Wave table definition
 */
typedef struct WaveTable {
  char name[WAVE_NAME_LEN];
  uint8_t data[WAVE_TABLE_LEN];
} WaveTable;


/**
 * Get an error message string from an error code.
 * 
 * @param error - Error code
 * @return Return pointer to message.
 */
const char* wt_errorMessage(uint8_t error);

/**
 * Load a wave table from ESP8266 filesystem.
 * 
 * @param wave - Pointer to a wavetable to load wave data into.
 * @param path - Path to file.
 * @return Result of load see WAVE_FILE_* for details.
 */
uint8_t wt_load(WaveTable* wave, char* path);

/**
 * Save a wave table to ESP8266 filesystem.
 * 
 * @param wave - Pointer to a wavetable to save.
 * @param path - Path to file.
 * @return Result of load see WAVE_FILE_* for details.
 */
uint8_t wt_save(WaveTable* wave, char* path);

/**
 * Set wave table to zero.
 */
void wt_zero(WaveTable* wave);

/**
 * Mirror the waveform
 */
void wt_mirror(WaveTable* wave);

/**
 * Invert the waveform
 */
void wt_invert(WaveTable* wave);

#endif //!_WAVE_TABLES__H
