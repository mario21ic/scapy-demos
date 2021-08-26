#!/usr/bin/env python
# Usage:   ./ipcalc.py ip prefix
# Example: ./ipcalc.py 192.168.10.15 20

import sys

from lib.clase import get_clase
from lib.rango import get_rango, get_direccion_red, get_direccion_broadcast, get_primera_direccion, get_ultima_direccion
from lib.net_host import get_net_host
from lib.mask import get_mask


my_ip = sys.argv[1]
my_prefix = int(sys.argv[2])
clase = get_clase(my_ip)
print("clase:", clase)

net_id, host_id = get_net_host(my_ip, clase)
print("net_id: %s - host_id: %s" % (net_id, host_id))

n = 32 - my_prefix
print("n:", n)
ips = (2**n)-2
print("ips:", ips)

my_mask = get_mask(my_prefix)
print("mask:", ".".join(my_mask))

direccion_red = ".".join(get_direccion_red(my_ip, n))
print("direccion de red:", direccion_red)

direccion_broadcast = ".".join(get_direccion_broadcast(my_ip, n))
print("direccion de broadcast:", direccion_broadcast)

print("primera direccion disponible:", get_primera_direccion(direccion_red))

print("ultima direccion disponible:", get_ultima_direccion(direccion_broadcast))

"""
Notes:
Inspirado en: http://labvirtual.webs.upv.es/ipcalc.html

TODO:
- Direccion de subred
- Direccion ip, mask y subred en binario
"""
