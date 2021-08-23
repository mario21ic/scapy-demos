#!/usr/bin/env python3

from scapy.all import *

"""
Note:
srbt only for bluetooth
srloop for n packages and times, for layer 2 srploop
"""

print("## Capa 3")
pkg3 = IP(dst="google.com")/ICMP(seq=[x for x in range(2)])
print(pkg3.show())
print(pkg3.summary())
ans3, unans3 = sr(pkg3)
#ans3 = sr1(pkg2) # only first answer
for x in ans3:
    print(x)
print(TCP in ans3)
print(ICMP in ans3)

print("## Capa 2")
#pkg2 = Ether()/IP(dst="google.com")/ICMP()
pkg2 = Ether()/IP(dst="google.com")/ICMP(seq=[x for x in range(2)])
print(pkg2.show2())
print(pkg2.summary())
ans2, unans2 = srp(pkg2)
#ans2 = srp1(pkg2) # only first answer
for x in ans2:
    print(x)
print(TCP in ans3)
print(ICMP in ans3)

