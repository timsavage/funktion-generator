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

ASM_NAME_CHARS = string.letters + string.digits + '_'


class WaveTable(object):
    """
    Represents a wave table, by default this is fixed size list of byte values.

    The length of the list is the wave length while the byte data type
    represents the Dynamic range which can be represented.

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
    wave_length = wave_functions.WAVE_LENGTH
    dynamic_range = wave_functions.DYNAMIC_RANGE

    @classmethod
    def read(cls, f):
        # Check file id
        file_id = f.read(4)
        if file_id != WAVE_HEADER_ID:
            raise Exception("File is missing wave ID.")

        # Read header and check version
        data = f.read(wave_header.size)
        version, checksum, length = wave_header.unpack(data)
        if version != WAVE_VERSION:
            raise Exception("Unknown file version.")

        # Load/parse data
        data = f.read(length)
        wave = [wave_sample.unpack_from(data, x)[0] for x in range(length)]

        # Confirm checksum
        if checksum != functools.reduce(operator.xor, wave):
            raise Exception("Invalid checksum.")

        return cls(wave)

    def __init__(self, wave=None):
        assert wave is None or len(wave) == self.wave_length

        self.modified = False
        self._table = wave or wave_functions.zero_wave()

    def __getitem__(self, idx):
        return self._table[idx]

    def __setitem__(self, idx, value):
        if not(0 <= value <= self.dynamic_range):
            raise ValueError("Value outside dynamic range.")
        self._table[idx] = value

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
        :param offset: List
        :type offset: list(byte)
        :return:
        """
        # Get data as a list
        wave = list(wave)

        # Check size of wave data
        if len(wave) + offset > self.wave_length:
            raise IndexError("Overflow of wave data.")

        self.modified = True

        # Copy into wave table
        for idx, sample in enumerate(wave):
            self[idx + offset] = sample

        return self

    def mirror(self):
        self.modified = True
        self._table = wave_functions.mirror_wave(self._table)

    def invert(self):
        self.modified = True
        self._table = wave_functions.invert_wave(self._table)

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
            f.write(sample.pack(s))

    def export_gcc_asm(self, name, f):
        """
        Export wave table as an GCC Assembler data table.
        """
        name = ''.join(c for c in name.replace(' ', '_') if c in ASM_NAME_CHARS)
        print("{}:".format(name), file=f)

        for r in range(0, self.wave_length / 16):
            samples = self._table[r * 16:(r + 1) * 16]
            print('\t.byte\t', ','.join("0x{:02X}".format(s) for s in samples), sep='', file=f)
