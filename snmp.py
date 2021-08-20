#!/usr/bin/env python3

import sys
from scapy.all import *

print("sending snmp....")

# print(lsc())
# print(help(sendp))

# Red / IP / TCP / App
pkg = Ether()/IP(dst="192.168.1.10")/SNMP()

#print(pkg.show())
print(pkg.show2())

# we use sendp because stp protocol is layer 2 instead 3
print(sendp(pkg, iface="en0"))

