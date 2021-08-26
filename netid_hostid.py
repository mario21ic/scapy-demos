#!/usr/bin/env python

import sys

from lib.clase import get_clase


my_ip = sys.argv[1]
octetos = my_ip.split(".")
clase = get_clase(my_ip)

net_id = None
host_id = None

print("clase:", clase)

if clase == "A":
    net_id = octetos[0]
    host_id = octetos[1:]
elif clase == "B":
    net_id = octetos[:2]
    host_id = octetos[2:]
elif clase == "C":
    net_id = octetos[:3]
    host_id = octetos[3:]
elif clase == "D":
    print("Multicast address")
elif clase == "E":
    print("Reserved for future use")

print("net_id: %s - host_id: %s" % (net_id, host_id))

