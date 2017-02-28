########################
DDS Generator - Firmware
########################

This is the firmware for the DDS (Direct Digital Synthesis) signal generator component. The firmware is designed for an ATMega328p MCU with Port D connected to an R-2R ladder based DAC.

The firmware is controlled via I2C on the default address of `0x42`, wave tables are included for the following wave forms:

- Sine
- Sawtooth
- Reverse Sawtooth
- Square
- Triangle

Future versions will include support for custom waveforms as well as a configurable PWM.


Building
--------

AVR-GCC and Make is required to build the source and avrdude to upload via an AVR ISP.

The following commands will build and upload the firmware::

        # Build and load firmware
        make up

        # Set correct fuses
        make fuse

For more info on the other make rules use the command `make help`.


I2C (TWI) Interface
-------------------

The firmware makes use of the built in TWI hardware. The I2C interface is the current active development area, the current code supports the following command scheme:

Requests are a single byte. The upper 4 bits represent the command and the lower 4 bits the argument: upper 4 bits represent the action:

- 0x10 - Load commands

  - 0x0 - Load Zero wave - Hack to turn "off" output
  - 0x1 - Load Sine wave
  - 0x2 - Load Square wave
  - 0x3 - Load Triangle wave
  - 0x4 - Load Sawtooth wave
  - 0x5 - Load Reverse Sawtooth wave

- 0x20 - Increase frequency

  - 0x0 - Noop
  - 0x1 - Increase frequency step by 1
  - 0x2 - Increase frequency step by 10
  - 0x3 - Increase frequency step by 100

- 0x30 - Decrease frequency

  - 0x0 - Noop
  - 0x1 - Decrease frequency step by 1
  - 0x2 - Decrease frequency step by 10
  - 0x3 - Decrease frequency step by 100

This design will require changes to support loading of custom waves, setting of specific step sizes (24bit value).


DDR Synthesis Design
--------------------

Is based around a 24bit step size over a 256 byte wave table.

Full details *TBA*.

