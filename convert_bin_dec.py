#!/usr/bin/env python

import sys

def bin_dec(mybinario) -> int:
    """
    bits_value = []
    for x in range(8):
        bits_value.append(2**x)
    bits_value.reverse()
    """
    bits_value = [2**x for x in range(8)]
    bits_value.reverse()

    result = 0
    x = 0
    for b in mybinario:
        if b=="1":
            result += int(bits_value[x])
        x+=1
    return result

if len(sys.argv)==5:
    for block in range(1, 5):
        print(bin_dec(sys.argv[block]), end=" ")
else:
    print("Usage:\n./convert_bin_dec.py 10000001 00001011 00001011 11101111")

print("")
