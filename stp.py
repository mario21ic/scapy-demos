#!/usr/bin/env python3

import sys
from scapy.all import *

print("sending stp....")

#pkg = Ether(dst="3c:06:30:0c:8b:67")/LLC()/STP()
pkg = Ether(dst="80:78:71:6d:45:40")/LLC()/STP()

#print(pkg.show())
print(pkg.show2())

# we use sendp because stp protocol is layer 2 instead 3
print(sendp(pkg, iface="en0"))

