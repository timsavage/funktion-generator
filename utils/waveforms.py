from __future__ import print_function, division, unicode_literals
import math

TAU = math.pi * 2


def render_wave(name, values):
	len_values = len(values)
	print("{0}_table:".format(name))
	for r in range(0, int(len_values / 16)):
		step = values[r * 16:(r + 1) * 16]
		print('\t.byte\t', ','.join("0x{:02X}".format(x) for x in step), sep='')
	print("")


def sine_func(x):
	return 127 + int(math.sin((x / 256.0) * TAU) * 127 + 0.5)


def triangle_func(x):
	if 0 <= x < 64:
		return 127 + x * 2
	elif 64 <= x < 192:
		return 255 - (x - 64) * 2
	elif x == 192:
		return 0
	else:
		return ((x - 192) * 2) - 1


def saw_tooth_func(x):
	return (127 + x) % 256


def rsaw_tooth_func(x):
	return (127 - x) % 256


def square_func(x):
	return 255 if x < 128 else 0


print('.org 0x100\t; Ensure lower 8 bits are all 0')
render_wave('sine', [sine_func(x) for x in range(256)])
render_wave('square', [square_func(x) for x in range(256)])
render_wave('triangle', [triangle_func(x) for x in range(256)])
render_wave('linear_ramp', [saw_tooth_func(x) for x in range(256)])
render_wave('rlinear_ramp', [rsaw_tooth_func(x) for x in range(256)])

