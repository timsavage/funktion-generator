#### Project configuration options ####

# Name of target controller
MCU = atmega328p

# Project name
PROJECT_NAME = funktion_gen

# MCU clock frequency - Higher the better an AVR can be run at 30Mhz.
# Remember to update the step constant if this value is changed
CLOCK_FREQ = 16000000UL  # 16 MHz
#CLOCK_FREQ = 20000000UL  # 20 MHz
#CLOCK_FREQ = 30000000UL  # 30 MHz

# DDS step constant
#
# This value is used to calculate the step size required to generate
# a waveform at the specified frequency. The value is defined as:
#
# DDS_FIXED_CONSTANT = (256 ^ 2 * ASM_LOOP_CYCLES) / CLOCK_FREQ
#
# The value of 256 ^ 3 is derived from the length of the waveform 
# table and the offset of the bits used to index into the waveform
# table. The offset is 256 << 16 (or 256 ^ 2)
#
# ASM_LOOP_CYCLES is the number of clock cycles required to complete 
# one cycle of the DDS generation loop, the current value is 9 clock 
# cycles.
#
# CLOCK_FREQ is the clock speed of the MCU in Hz.
#
# It is easier to pre-calculate this value, this Google Sheets document
# provides all the nessasary calulations:
#
# https://docs.google.com/spreadsheets/d/1Oab6_2TZ5SzAQHbTxMHLZFGgJnOQwO2SQYt80mpjkCc/edit?usp=sharing
DDS_FIXED_CONSTANT = 9.437184  # 16Mhz
#DDS_FIXED_CONSTANT = 7.5497472  # 20Mhz
#DDS_FIXED_CONSTANT = 5.0331648  # 30Mhz

# Source files
SRC = main.S

# Additional include paths
INCLUDES = 

# Libraries to link
LIBS =

# Optimisation
# use s (size opt), 1, 2, 3 or 0 (off)
OPTIMIZE = 1

# AVR Dude programmer
AVRDUDE_PROGRAMMER = usbtiny

#### End project configuration ####


#### Flags

DEFINES = -DF_CPU=$(CLOCK_FREQ) -DDDS_FIXED_CONSTANT=$(DDS_FIXED_CONSTANT)

# Compiler
override CFLAGS = -I. $(INCLUDES) -g -O$(OPTIMIZE) -mmcu=$(MCU) $(DEFINES) \
		-Wall -Werror -Wl,-section-start=.WaveBuffer=0x00800300 \
		-pedantic -pedantic-errors -std=gnu99 \
		-fpack-struct -fshort-enums -funsigned-char -funsigned-bitfields -ffunction-sections

# Assembler
override ASMFLAGS = -I. $(INCLUDES) -mmcu=$(MCU) $(DEFINES) -x assembler-with-cpp

# Linker
override LDFLAGS = -Wl,-Map,$(TRG).map 

#### Executables

CC = avr-gcc
OBJCOPY = avr-objcopy
OBJDUMP = avr-objdump
SIZE = avr-size
AVRDUDE = avrdude
REMOVE = rm -f


#### Target Names

TRG = $(PROJECT_NAME).out
DUMPTRG = $(PROJECT_NAME).s

HEXROMTRG = $(PROJECT_NAME).hex
HEXTRG = $(HEXROMTRG) $(PROJECT_NAME).ee.hex
GDBINITFILE = gdbinit-$(PROJECT_NAME)

# Filter files by type
CFILES = $(filter %.c, $(SRC))
ASMFILES = $(filter %.S, $(SRC))

# Generate list of object files
OBJS = $(CFILES:.c=.c.o) $(ASMFILES:.S=.S.o)

# Define .lst files
LST = $(filter %.lst, $(OBJS:.o=.lst))


# Build all
all: $(TRG)
	
stats: $(TRG)
	$(OBJDUMP) -h $(TRG)
	$(SIZE) $(TRG)

hex: $(HEXTRG)

upload: hex
	$(AVRDUDE) -c $(AVRDUDE_PROGRAMMER) -p $(MCU) -U flash:w:$(HEXROMTRG)

fuses: 
	$(AVRDUDE) -c $(AVRDUDE_PROGRAMMER) -p $(MCU) -U lfuse:w:0xf7:m -U hfuse:w:0xd9:m

install: fuses upload

# Linking
$(TRG): $(OBJS) 
	$(CC) $(LDFLAGS) -o $(TRG) $(OBJS)

# Generate object files
%.c.o: src/%.c
	$(CC) $(CFLAGS) -c $< -o $@

%.S.o: src/%.S
	$(CC) $(ASMFLAGS) -c $< -o $@

# Generate hex
%.hex: %.out
	$(OBJCOPY) -j .text -j .data -O ihex $< $@

%.ee.hex: %.out
	$(OBJCOPY) -j .eeprom --change-section-lma .eeprom=0 -O ihex $< $@

# GDB Init file
gdbinit: $(GDBINITFILE)
	@echo "file $(TRG)" > $(GDBINITFILE)
	@echo "target remote localhost:1212" >> $(GDBINITFILE)
	@echo "load" >> $(GDBINITFILE)
	@echo "break main" >> $(GDBINITFILE)
	@echo "continue" >> $(GDBINITFILE)
	@echo
	@echo "Use 'avr-gdb -x $(GDBINITFILE)'"

clean:
	$(REMOVE) $(TRG) $(TRG).map
	$(REMOVE) $(OBJS)
	$(REMOVE) $(GDBINITFILE)
	$(REMOVE) *.hex

