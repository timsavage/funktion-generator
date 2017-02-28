##########################
Funktion Generator - Utils
##########################

Some Python utility programs for automate generation and calculations of DDS parameters.

dds-calc
========

Calculates the constant used to generate waveforms at a particular frequency. This script includes other commands to not only generate the constant but to also output the step size for a particular frequency (along with the rounding error associated with that particular frequency) and the 24bit value split into hex encoded bytes for insertion into the asm code.

Usage, caclulate the step size for a 1KHz wave, with 24bit bytes split out::

    $ ./dds-calc 1 KHz -d    
    ----------------------------------------
    Clock Frequency:  16MHz (16000000.0Hz)
    Clocks per Cycle: 8
    Wave table size:  256
    ----------------------------------------
    Step Constant:    8.388608
    Step size:        8389 @ 1.0KHz
    Step size bytes:  0x00, 0x20, 0xC5

    Actual Freq:      1000.046730Hz
    Freq Error:       0.004673%
    ----------------------------------------
    
    
For more help::

    $ ./dds-calc --help
    usage: dds-calc [-h] [-c CLOCK_FREQ] [--cfreq-unit {Hz,KHz,MHz}]
                    [-p CLOCKS_PER_CYCLE] [-t TABLE_SIZE] [-d]
                    [TARGET_FREQ] [{Hz,KHz,MHz}]

    Tool for calculating frequency constants

    positional arguments:
      TARGET_FREQ           Calculate a step size value for a target frequency
      {Hz,KHz,MHz}          Unit of target frequency, default is Hz

    optional arguments:
      -h, --help            show this help message and exit
      -c CLOCK_FREQ, --cfreq CLOCK_FREQ
                            Frequency of MCU
      --cfreq-unit {Hz,KHz,MHz}
                            Unit/Multiplier of cfreq value, default is Mhz
      -p CLOCKS_PER_CYCLE, --cpc CLOCKS_PER_CYCLE
                            Number of clock ticks in each cycle of DDS loop.
      -t TABLE_SIZE, --table-size TABLE_SIZE
                            Size of DDS wave table (this should be 256)
      -d, --decompose-step  Decompose step constant into individual bytes


wavetables.py
=============

Script that creates the pre-generated wave-tables that are include in the firmware. Executing will output assembler .byte tables to *stdout*.
