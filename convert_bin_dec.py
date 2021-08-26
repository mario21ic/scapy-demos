#!/usr/bin/env python

import sys

from lib.convert import bin_dec


if len(sys.argv)==5:
    for block in range(1, 5):
        print(bin_dec(sys.argv[block]), end=" ")
else:
    print("Usage:\n./convert_bin_dec.py 10000001 00001011 00001011 11101111")

print("")
