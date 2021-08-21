#!/usr/bin/env python3

import sys
from scapy.all import *

dst_ip = sys.argv[1]

#pkg = Loopback()/IP(dst=sys.argv[1])/UDP(sport=666, dport=666)/"xD"
pkg = IP(src="127.0.0.1", dst=sys.argv[1])/UDP(sport=666, dport=666)/"xD"

print(pkg.show())

print(send(pkg))

