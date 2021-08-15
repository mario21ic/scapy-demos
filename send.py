#!/usr/bin/env python3

import sys
from scapy.all import *

p=IP(dst="14b5e61598bb.ngrok.io")/TCP(dport=80)/Raw(load="hello python")
print(p)
print(p.show())

send(p)

