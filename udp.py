#!/usr/bin/env python3

import sys
from scapy.all import *

dst_ip = sys.argv[1]

#pkg = Loopback()/IP(dst=sys.argv[1])/UDP(sport=666, dport=666)/"xD"
pkg = IP(dst=dst_ip)/UDP(sport=666, dport=666)/"xD"

print(pkg.show())

print(send(pkg))

print(pkg.summary())
