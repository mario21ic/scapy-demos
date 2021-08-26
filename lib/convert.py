#!/usr/bin/env python

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
