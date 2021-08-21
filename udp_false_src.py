#!/usr/bin/env python3

import sys
from scapy.all import *

src_mac = sys.argv[1]
src_ip = sys.argv[2]
dst_ip = sys.argv[3]

#pkg = IP(src=src_ip, dst=dst_ip)/UDP(sport=666, dport=666)/"xD"
pkg = Ether(src=src_mac)/IP(src=src_ip, dst=dst_ip)/UDP(sport=666, dport=666)/"xD"

print(pkg.show())

#print(send(pkg))
print(sendp(pkg))

print(pkg.summary())
