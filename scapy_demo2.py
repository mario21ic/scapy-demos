#!/usr/bin/env python3

import sys
from scapy.all import *

p = IP(dst="github.com")/ICMP()
print(p)

r = sr1(p)
print(r)

