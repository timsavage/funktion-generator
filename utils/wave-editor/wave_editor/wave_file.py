from __future__ import absolute_import, print_function

import functools
import string
import struct
import operator

from wave_editor import wave_functions

WAVE_VERSION = 1
WAVE_HEADER_ID = 'wave'
wave_header = struct.Struct("BBH")
wave_sample = struct.Struct("B")


class WaveFileError(Exception):
    pass


class WaveTable(object):
    """
    Represents a wave table, by default this is fixed size list of signed byte 
    values. The length of the table is the wave length while the byte data type
    represents the Dynamic range which can be represented. 
    
    For writing to a file samples are encoded around a 0 or origin value of 
    0x80 allowing for a maximum sample value of +127 (encoded as 0xFF) and a 
    minimum of -128 (encoded as 0x00).  

    The on disk representation::

            | Header |
        0000|XXXXVCLL|
        0008|DDDDDDDD|
        000F|DDDDDDDD|
            | ...... |
        0108|DDDDDDDD|

    X = Header token value "wave"
    V = File version
    C = Checksum of table (XOR)
    L = Length of table

    """
    FILE_ORIGIN = 0x80

    @classmethod
    def read(cls, f):
        # Check file id
        file_id = f.read(4)
        if file_id != WAVE_HEADER_ID:
            raise WaveFileError("File is missing wave ID.")

        # Read header and check version
        data = f.read(wave_header.size)
        version, checksum, length = wave_header.unpack(data)
        if version != WAVE_VERSION:
            raise WaveFileError("Unknown file version.")

        # Load/parse data
        data = f.read(length)
        wave = [wave_sample.unpack_from(data, x)[0]for x in range(length)]

        # Confirm checksum
        if checksum != functools.reduce(operator.xor, wave):
            raise WaveFileError("Invalid checksum.")

        return cls(w - wave_functions.ORIGIN for w in wave)

    def __init__(self, wave=None):
        wave = list(wave or wave_functions.zero_wave())
        assert wave is None or len(wave) == wave_functions.WAVE_LENGTH

        self.modified = False
        self._table = wave

    def __getitem__(self, idx):
        return self._table[idx]

    def __setitem__(self, idx, value):
        if not (-0x80 <= value <= 0x7F):
            raise ValueError("Value outside dynamic range.")
        self._table[idx] = value

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        return iter(self._table)

    def clear_modified(self):
        self.modified = False

    def zero(self):
        """
        Zero the wave
        """
        return self.insert(wave_functions.zero_wave())

    def insert(self, wave, offset=0):
        """
        Insert wave data into the wave table. Unlike a list inserting wave
        data overwrites existing wave data.

        :param wave: Iterable of bytes to insert into the wave table, this
            data must be no longer than the Wavelength.
        :type wave: iter<byte>
        :param offset: Offset in wave table to begin insert
        :type offset: int

        """
        # Get data as a list
        wave = list(wave)

        # Check size of wave data
        if len(wave) + offset > wave_functions.WAVE_LENGTH:
            raise IndexError("Overflow of wave data.")

        self.modified = True

        # Copy into wave table
        for idx, sample in enumerate(wave):
            self[idx + offset] = sample

        return self

    def merge(self, wave, offset=0):
        """
        Merge wave data into the wave table. This involves generating an
        average of the two waves.

        The processes is simple, add the two waves before dividing by two
        producing an average of the two wave forms.

        :param wave: Iterable of bytes to insert into the wave table, this
            data must be no longer than the Wavelength.
        :type wave: iter<byte>
        :param offset: Offset in wave table to begin merge
        :type offset: int

        """
        # Get data as a list
        wave = list(wave)

        # Check size of wave data
        if len(wave) + offset > wave_functions.WAVE_LENGTH:
            raise IndexError("Overflow of wave data.")

        self.modified = True

        # Merge into wave table
        for idx, sample in enumerate(wave):
            self[idx + offset] = (self[idx + offset] + sample) >> 1

        return self

    def write(self, f):
        """
        Write wave table to a file (or file like) object
        """
        length = len(self._table)
        checksum = functools.reduce(operator.xor, self._table)

        # Write file ID
        f.write(WAVE_HEADER_ID)

        # Write header
        f.write(wave_header.pack(WAVE_VERSION, checksum, length))

        # Write samples
        sample = struct.Struct("B")
        for s in self._table:
            f.write(sample.pack(s + 0x80))


class ExportAsmFormatter(object):
    """
    Export a wave table to ASM source.

    Supports both GCC and AVR Assembler (AVRASM2) style ASM style.
    """
    ASM_STYLE_GCC = 'GCC'
    ASM_STYLE_AVRASM2 = 'AVRASM2'

    ASM_LABEL_CHARS = string.letters + string.digits + '_'

    GCC_ROW_PREFIX = '\t.byte\t'
    AVRASM2_ROW_PREFIX = '\t.DB\t'

    def __init__(self, wave_table, label_name=None, asm_style=ASM_STYLE_GCC):
        """
        Initialise formatter

        :param wave_table: Wave table to format
        :type wave_table: WaveTable
        :param label_name: Label to apply to wave table
        :param asm_style: Style of ASM to generate; default is GCC

        """
        self.wave_table = wave_table
        self.label_name = label_name
        self.asm_style = asm_style

    def __call__(self, f):
        if self.label_name:
            label_name = ''.join(c for c in self.label_name.replace(' ', '_') if c in self.ASM_LABEL_CHARS)
            print("{}:".format(label_name), file=f)

        if self.asm_style == self.ASM_STYLE_GCC:
            prefix = self.GCC_ROW_PREFIX
        else:
            prefix = self.AVRASM2_ROW_PREFIX

        for r in range(0, wave_functions.WAVE_LENGTH / 16):
            samples = self.wave_table[r * 16:(r + 1) * 16]
            print(prefix, ','.join("0x{:02X}".format(wave_functions.ORIGIN + s) for s in samples), sep='', file=f)


class ExportCFormatter(object):
    """
    Export a wave table to c source.
    """
    VARIABLE_NAME_CHARS = string.letters + string.digits + '_'

    def __init__(self, wave_table, variable_name):
        """
        :type wave_table: WaveTable
        :param variable_name: Name of the variable holding wave table
        """
        self.wave_table = wave_table
        self.variable_name = variable_name

    def __call__(self, f):
        variable_name = ''.join(c for c in self.variable_name.replace(' ', '_') if c in self.VARIABLE_NAME_CHARS)
        print(
            "/**\n"
            " * Exported from Wave Editor\n"
            " */\n\n"
            "#include <stdint.h>\n\n"
            "const uint8_t {}[] = {{".format(variable_name),
            file=f
        )

        for r in range(0, wave_functions.WAVE_LENGTH / 16):
            samples = self.wave_table[r * 16:(r + 1) * 16]
            print('\t', ','.join("0x{:02X}".format(wave_functions.ORIGIN + s) for s in samples), ',', sep='', file=f)

        print("};", file=f)
