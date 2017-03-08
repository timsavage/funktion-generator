from __future__ import division, print_function

import math

DYNAMIC_RANGE = 0xFF
WAVE_LENGTH = 0xFF

# The useful circle constant!
TAU = math.pi * 2


class WaveGenerator(object):
    def __init__(self, function):
        """
        Initialise function generator

        :param function: Callable function to generate a waveform.

        """
        self.function = function
        self.dynamic_range = DYNAMIC_RANGE
        self.wave_length = WAVE_LENGTH

    def __iter__(self):
        args = (self.dynamic_range, self.wave_length)
        for x in range(0, self.wave_length + 1):
            yield self.function(x, *args)


def sine_wave_function(x, dynamic, _):
    origin = dynamic >> 1
    return origin + int(math.sin((x / float(dynamic)) * TAU) * origin + 0.5)


def square_wave_function(x, dynamic, length):
    half_wave = length >> 1
    return dynamic if x <= half_wave else 0


def saw_tooth_function(x, dynamic, _):
    origin = dynamic >> 1
    return (origin + x) % dynamic


def reverse_saw_tooth_function(x, dynamic, _):
    origin = dynamic >> 1
    return (origin - x) % dynamic


def triangle_wave_function(x, dynamic, length):
    origin = dynamic >> 1
    half_wave = length >> 1
    quarter_wave = length >> 1
    three_quarter_wave = half_wave + quarter_wave
    if 0 <= x < quarter_wave:
        return origin + x * 2
    elif quarter_wave <= x < three_quarter_wave:
        return dynamic - (x - quarter_wave) * 2
    else:
        return ((x - three_quarter_wave) * 2) - 1


def invert_wave(wave):
    """
    Invert the wave or mirror about the origin.
    """
    return [DYNAMIC_RANGE - x for x in wave]


def mirror_wave(wave):
    """
    Invert the wave about half a wave length
    """
    return list(reversed(wave))


if __name__ == '__main__':
    wave = list(WaveGenerator(saw_tooth_function))
    print(wave)
    from collections import Counter

    wave_counter = Counter(wave)
    print("Summary:", wave_counter)
    print("Most Common:", wave_counter.most_common())
    print("Length:", sum(wave_counter.values()))
