from __future__ import division, print_function

import math
import os

# Constants
DYNAMIC_RANGE = 0x100
ORIGIN = DYNAMIC_RANGE >> 1
MAX_OFFSET = 0x7F
WAVE_LENGTH = 0x100
TAU = math.pi * 2  # The useful circle constant!


def zero_wave():
    """
    A flat line about the origin.
    """
    return [0] * WAVE_LENGTH


def sine_wave():
    """
    Generate a sine wave.
    """
    return [int(math.sin((x / WAVE_LENGTH) * TAU) * MAX_OFFSET + 0.5) for x in range(WAVE_LENGTH)]


def square_wave():
    """
    Generate a square wave.
    """
    half_wave = WAVE_LENGTH >> 1
    return [MAX_OFFSET if x < half_wave else -MAX_OFFSET for x in range(WAVE_LENGTH)]


def triangle_wave():
    """
    Generate a triangle wave.
    """
    half_wave = WAVE_LENGTH >> 1
    quarter_wave = half_wave >> 1
    three_quarter_wave = half_wave + quarter_wave

    def wave_func(x):
        if 0 <= x < quarter_wave:
            return x << 1
        elif quarter_wave <= x < three_quarter_wave:
            return (MAX_OFFSET - x) << 1
        else:
            return -0x80 + ((x - three_quarter_wave) << 1)

    return [wave_func(x) for x in range(WAVE_LENGTH)]


def sawtooth_wave():
    """
    Generate a sawtooth wave.
    """
    return [x - 0x80 for x in range(WAVE_LENGTH)]


def reverse_sawtooth_wave():
    """
    Generate a reverse sawtooth wave.
    """
    return [0x7F - x for x in range(WAVE_LENGTH)]


def noise():
    """
    Generate noise
    """
    return [ord(x) - 0x80 for x in os.urandom(WAVE_LENGTH)]


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


def rectify_wave(wave):
    """
    Rectify the wave so the entire waveform is able the origin
    """
    return [math.fabs(x) for x in wave]


def normalise_wave(wave):
    """
    Scale wave to utilise the full dynamic range
    """
    rectified = rectify_wave(wave)
    max_offset = max(rectified)
    scale = MAX_OFFSET / (1.0 * max_offset)
    return [int(x * scale) for x in wave]

 
def centre_wave(wave):
    """
    Center a wave about the origin
    """
    above_origin = [x - ORIGIN for x in wave if x >= ORIGIN]
    max_range = max(above_origin) if above_origin else 0
    below_origin = [ORIGIN - x for x in wave if x < ORIGIN]
    min_range = max(below_origin) if below_origin else 0
    offset = (max_range - min_range) >> 1
    return [x - offset for x in wave]
