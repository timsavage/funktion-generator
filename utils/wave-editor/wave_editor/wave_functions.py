from __future__ import division, print_function

import math

DYNAMIC_RANGE = 0xFF
WAVE_LENGTH = 256

TAU = math.pi * 2  # The useful circle constant!


def zero_wave():
    """
    A flat line about the origin.
    """
    origin = DYNAMIC_RANGE >> 1
    return [origin for _ in range(WAVE_LENGTH)]


def sine_wave():
    """
    Generate a sine wave.
    """
    origin = DYNAMIC_RANGE >> 1
    f_dynamic = float(DYNAMIC_RANGE)
    return [origin + int(math.sin((x / f_dynamic) * TAU) * origin + 0.5) for x in range(WAVE_LENGTH)]


def square_wave():
    """
    Generate a square wave.
    """
    half_wave = WAVE_LENGTH >> 1
    high = DYNAMIC_RANGE,
    low = 0
    return [high if x < half_wave else low for x in range(WAVE_LENGTH)]


def triangle_wave():
    """
    Generate a triangle wave.
    """
    origin = DYNAMIC_RANGE >> 1
    half_wave = WAVE_LENGTH >> 1
    quarter_wave = half_wave >> 1
    three_quarter_wave = half_wave + quarter_wave

    def wave_func(x):
        if 0 <= x < quarter_wave:
            return origin + x * 2
        elif quarter_wave <= x < three_quarter_wave:
            return DYNAMIC_RANGE - (x - quarter_wave) * 2
        else:
            return ((x - three_quarter_wave) * 2) - 1

    return [wave_func(x) for x in range(WAVE_LENGTH)]


def sawtooth_wave():
    """
    Generate a sawtooth wave.
    """
    origin = DYNAMIC_RANGE >> 1
    return [(origin + x) % DYNAMIC_RANGE for x in range(WAVE_LENGTH)]


def reverse_sawtooth_wave():
    """
    Generate a reverse sawtooth wave.
    """
    origin = DYNAMIC_RANGE >> 1
    return [(origin - x) % DYNAMIC_RANGE for x in range(WAVE_LENGTH)]


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
