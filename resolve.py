#!/usr/bin/env python3

import sys
from scapy.all import *

print("pinging the target....")
#ip = sys.argv[1]
target="www.google.com"
#target="www.target.com/30"
ip=IP(dst=target)
print("ip:", ip)
#for p in ip:
#  print(p)
