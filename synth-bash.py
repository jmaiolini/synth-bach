#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Jacopo Maiolini and Matteo Santilli"
__license__ = "MIT"

import argparse
from synth.synth import Synthetizer

def main():
    parser = argparse.ArgumentParser(description="Synth command line interface.")
    parser.add_argument(
        "--octave",
        type=int,
        default=0,
        help="Insert the Octave you want to play.",
    )

    parser.set_defaults(cached=True)

    args = parser.parse_args()
    synth = Synthetizer()
    synth.start()



if __name__ == "__main__":
    """ Welcome to the Ba(s)ch Synth """
    main()
