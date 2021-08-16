#!/usr/bin/env python3

import sys
from scapy.all import *

# Red / IP / TCP / App
pkg = Ether()/IP(dst="google.com")/TCP(dport=80)/"GET /HTTP 1.1"
print(send(pkg))
