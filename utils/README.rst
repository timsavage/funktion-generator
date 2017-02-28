##########################
Funktion Generator - Utils
##########################

Some Python utility programs for automate generation and calculations of DDS parameters.

dds-calc.py
===========

Calculates the constant used to generate waveforms at a particular frequency. This script includes other commands to not only generate the constant but to also output the step size for a particular frequency (along with the rounding error associated with that particular frequency) and the 24bit value split into hex encoded bytes for insertion into the asm code.

Usage, caclulate the step size for a 1KHz wave, with 24bit bytes split out::

    ./dds-calc.py 1 KHz -d    
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


wavetables.py
=============

Script that creates the pre-generated wave-tables that are include in the firmware. Executing will output assembler .byte tables to *stdout*.
