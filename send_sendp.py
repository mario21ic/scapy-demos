#!/usr/bin/env python3

from scapy.all import *


pkg2 = Ether()/IP(dst="google.com")/ICMP()
print(pkg2.show())
# para capa 2
print(sendp(pkg2))

pkg3 = IP(dst="google.com")/ICMP()
print(pkg3.show())
# para capa 3
print(sendp(pkg3))

