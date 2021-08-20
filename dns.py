#!/usr/bin/env python3

import sys
from scapy.all import *

print("resolve the target....")
target = sys.argv[1]

# answer = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=target)),verbose=0)
dns_req = IP(dst="192.168.1.10")/\
    UDP(dport=53)/\
    DNS(rd=1,qd=DNSQR(qname=target))

print(dns_req.show2(dns_req))

answer = sr1(dns_req, verbose=0)

print(answer[DNS].summary())
