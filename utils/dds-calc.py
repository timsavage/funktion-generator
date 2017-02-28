#!/usr/bin/env python
from __future__ import print_function, division, unicode_literals

import argparse
import math


FREQ_SCALE = {
    "Hz": 1.0,
    "KHz": 1000.0,
    "MHz": 1000000.0,
}


def get_args():
    parser = argparse.ArgumentParser("Freq", description="Tool for calculating frequency constants")
    parser.add_argument("-c", "--cfreq", dest="clock_freq", default=16, type=float,
                        help="Frequency of MCU")
    parser.add_argument("--cfreq-unit", dest='freq_unit', choices=FREQ_SCALE.keys(), default="MHz",
                        help="Unit/Multiplier of cfreq value, default is Mhz")
    parser.add_argument("-p", "--cpc", dest="clocks_per_cycle", default=8, type=int,
                        help="Number of clock ticks in each cycle of DDS loop.")
    parser.add_argument("-t", "--table-size", dest="table_size", default=256, type=int,
                        help="Size of DDS wave table (this should be 256)")

    parser.add_argument("TARGET_FREQ", nargs="?", type=float,
                        help="Calculate a step size value for a target frequency")
    parser.add_argument("TARGET_UNIT", nargs="?", default="Hz", choices=FREQ_SCALE.keys(),
                        help="Unit of target frequency, default is Hz")
    parser.add_argument("-d", "--decompose-step", dest="decompose_step", action="store_true",
                        help="Decompose step constant into individual bytes")

    return parser.parse_args()


def main():
    opts = get_args()

    cfreq = opts.clock_freq * FREQ_SCALE[opts.freq_unit]
    cpc = opts.clocks_per_cycle
    wts = opts.table_size

    print("-" * 40)
    print("Clock Frequency:  {}{} ({}Hz)".format(opts.clock_freq, opts.freq_unit, cfreq))
    print("Clocks per Cycle: {}".format(cpc))
    print("Wave table size:  {}".format(wts))
    print("-" * 40)

    step_constant = (wts * math.pow(wts, 2) * cpc) / cfreq
    print("Step Constant:    {:0.6f}".format(step_constant))

    if opts.TARGET_FREQ:
        target_freq = opts.TARGET_FREQ * FREQ_SCALE[opts.TARGET_UNIT]
        step_size = int((target_freq * step_constant) + 0.5)
        actual_freq = step_size / step_constant
        error = ((actual_freq/target_freq) - 1) * 100

        print("Step size:        {} @ {}{}".format(step_size, opts.TARGET_FREQ, opts.TARGET_UNIT))
        if opts.decompose_step:
            print("Step size bytes:  {}, {}, {}".format(
                *['0x{:02X}'.format(step_size >> (b * 8) & 0xFF) for b in range(2, -1, -1)]
            ))

        print()
        print("Actual Freq:      {:0.6f}Hz".format(actual_freq))
        print("Freq Error:       {:0.6f}%".format(error))

    print("-" * 40)


if __name__ == '__main__':
    main()

