#!/usr/bin/env python3

import sys
from scapy.all import *

print("pinging the target....")

ip = sys.argv[1]
icmp = IP(dst=ip)/ICMP()
resp = sr1(icmp,timeout=10)

result = "This host is up!"
if resp == None:
    result = "This host is down"

print(result)
