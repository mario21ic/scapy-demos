import copy

from .convert import dec_bin, bin_dec, ip_bin, fill_last_n
from .mask import group_by8


def get_n(my_prefix):
    return 32 - my_prefix

def get_ips_n(my_prefix):
    return (2**get_n(my_prefix))-2

def get_direccion_red(my_ip, n):
    bits = ip_bin(my_ip)
    #print("bits", bits)

    bits = fill_last_n(bits, n, "0")
    #print("bits", bits)

    blocks = group_by8(bits)
    #print("blocks", blocks)
    result = []
    for b in blocks:
        result.append(str(bin_dec(b)))
    #print("result", result)
    return ".".join(result)

def get_direccion_broadcast(my_ip, n):
    bits = ip_bin(my_ip)
    #print("bits", bits)

    bits = fill_last_n(bits, n, "1")
    #print("bits", bits)
    blocks = group_by8(bits)
    #print("blocks", blocks)
    result = []
    for b in blocks:
        result.append(str(bin_dec(b)))
    #print("result", result)
    return ".".join(result)

def get_primera_direccion(direccion_red):
    bits = ip_bin(direccion_red)
    bits = fill_last_n(bits, 1, "1")
    #print("bits", bits)
    blocks = group_by8(bits)
    result = []
    for b in blocks:
        result.append(str(bin_dec(b)))
    #print("result", result)
    return ".".join(result)

def get_ultima_direccion(direccion_broadcast):
    bits = ip_bin(direccion_broadcast)
    bits = fill_last_n(bits, 1, "0")
    #print("bits", bits)
    blocks = group_by8(bits)
    result = []
    for b in blocks:
        result.append(str(bin_dec(b)))
    #print("result", result)
    return ".".join(result)

def get_rango(octeto):
    inicio = copy.copy(octeto)
    fin = copy.copy(octeto)
    if type(octeto) is not list:
        inicio = [octeto]
        fin = [octeto]
    for x in range(4-len(inicio)):
        inicio.append("0")
        fin.append("255")
    return [".".join(inicio), ".".join(fin)]
