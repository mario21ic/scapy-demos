#!/usr/bin/env python3

import sys
from scapy.all import *

p=IP(dst="192.168.1.1")/ICMP()/"hello python"
print(p)
print(p.show())

sr1(p)

