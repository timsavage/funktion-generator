from __future__ import absolute_import

import functools
import struct
import operator

from wave_editor import wave_functions

WAVE_HEADER_ID = 'wave'
wave_header = struct.Struct("BBH")
wave_sample = struct.Struct("B")


class WaveTable(object):
    """
    Represents a wave table, by default this is fixed size list of byte values.

    The length of the list is the wave length while the byte data type
    represents the Dynamic range which can be represented.

    The on disk representation::

            | Header |
        0000|XXXXXVLC|
        0008|DDDDDDDD|
        000F|DDDDDDDD|
            | ...... |
        0108|DDDDDDDD|

    X = Header token value ".wave"
    V = File version
    L = Length of table
    C = Checksum of table (XOR)

    """
    _wave_length = wave_functions.WAVE_LENGTH
    _dynamic_range = wave_functions.DYNAMIC_RANGE

    @classmethod
    def load(cls, f):
        # Check file id
        file_id = f.read(4)
        if file_id != WAVE_HEADER_ID:
            raise Exception("File is missing wave ID.")

        # Read header and check version
        data = f.read(wave_header.size)
        version, checksum, length = wave_header.unpack(data)
        if version != 1:
            raise Exception("Unknown file version.")

        # Load/parse data
        data = f.read(length)
        wave = [wave_sample.unpack_from(data, x)[0] for x in range(length)]

        # Confirm checksum
        if checksum != functools.reduce(operator.xor, wave):
            raise Exception("Invalid checksum.")

        return cls(wave)

    def __init__(self, wave=None):
        assert wave is None or len(wave) == self._wave_length

        self._table = wave or wave_functions.zero_wave()

    def __getitem__(self, idx):
        return self._table[idx]

    def __setitem__(self, idx, value):
        if not(0 <= value <= self._dynamic_range):
            raise ValueError("Value outside dynamic range.")
        self._table[idx] = value

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
        if len(wave) + offset > self._wave_length:
            raise IndexError("Overflow of wave data.")

        # Copy into wave table
        for idx, sample in enumerate(wave):
            self[idx + offset] = sample

        return self

    def save(self, f):
        """
        Save wave table to a file (or file like) object
        """
        version = 1
        length = len(self._table)
        checksum = functools.reduce(operator.xor, self._table)

        # Write file ID
        f.write(WAVE_HEADER_ID)

        # Write header
        f.write(wave_header.pack(version, checksum, length))

        # Write samples
        sample = struct.Struct("B")
        for s in self._table:
            f.write(sample.pack(s))
