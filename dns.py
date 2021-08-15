#!/usr/bin/env python3

import sys
from scapy.all import *

print("resolve the target....")
target = sys.argv[1]

answer = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=target)),verbose=0)
print(answer[DNS].summary())
