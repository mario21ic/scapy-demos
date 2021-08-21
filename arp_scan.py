#!/usr/bin/env python3

from scapy.all import *

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"),timeout=2)
print(ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") ) )
#arping("192.168.1.*")

