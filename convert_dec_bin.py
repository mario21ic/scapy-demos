#!/usr/bin/env python
# Usage: ./convert_dec_bin.py 128.11.3.31

import sys


def dec_bin(mydecimal):
    bits_value = [2**x for x in range(8)]
    bits_value.reverse()

    result = ""
    suma = 0
    for d in bits_value:
        suma = suma + int(d)
        if suma <= mydecimal:
            result += "1"
        else:
            suma = suma - d
            result += "0"
    return result

mydecimal = sys.argv[1].split(".")
if len(mydecimal) == 4:
    for block in mydecimal:
        print(dec_bin(int(block)), end=" ")
else:
    print("Usage:\n ./convert_dec_bin.py 128.11.3.31")

print("")

