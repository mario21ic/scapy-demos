#!/usr/bin/env python3

import sys
from scapy.all import *

# Red / IP / TCP / App
# Debe fallar porque invertirmos el orden
send(ICMP(type=8)/IP(dst="192.168.1.1"), iface="lo0")


