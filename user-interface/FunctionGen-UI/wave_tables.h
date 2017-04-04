/**
 * wave_tables.h
 * 
 * Definition of wave table structure and data tables.
 * 
 */
#ifndef _WAVE_TABLES__H
#define _WAVE_TABLES__H

#include <stdint.h>

const size_t WAVE_NAME_LEN = 17; // 16 Chars

const size_t WAVE_TABLE_MAX = 0xFF;
const size_t WAVE_TABLE_LEN = WAVE_TABLE_MAX + 1;


/**
 * Wave table definition
 */
typedef struct WaveTable {
  char name[WAVE_NAME_LEN];
  uint8_t data[WAVE_TABLE_LEN];
} WaveTable;


/**
 * Builtin waves
 */
const uint8_t WAVE_ZERO = 0;
const uint8_t WAVE_SINE = 1;
const uint8_t WAVE_SQUARE = 2;
const uint8_t WAVE_TRIANGLE = 3;
const uint8_t WAVE_SAWTOOTH = 4;
const uint8_t WAVE_RSAWTOOTH = 5;
const uint8_t WAVE_BUILTIN_COUNT = WAVE_RSAWTOOTH + 1;

/**
 * Load a builtin wave into a wave table.
 */
void loadBuiltinWave(WaveTable* wave, uint8_t waveID);

/**
 * Custom waves
 */

/**
 * Store a wave table into a storage slot.
 */
void storeWave(WaveTable* wave, uint8_t slotID);

/**
 * Load a wave table from a storage slot.
 */
void loadWave(WaveTable* wave, uint8_t slotID);


/**
 * Manipulate waves
 */

void mirrorWave(WaveTable* wave);
void invertWave(WaveTable* wave);

#endif //!_WAVE_TABLES__H
