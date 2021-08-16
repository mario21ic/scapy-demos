#!/usr/bin/env python3

import sys
from scapy.all import *

#ip = IP(src="127.1.2.3", dst="192.168.1.10", ttl=128, tos=9)
ip = IP(src=sys.argv[1], dst="192.168.1.10", ttl=128, tos=9)
print(ip.show())
print(ip.show2())

print(send(ip/ICMP()))

