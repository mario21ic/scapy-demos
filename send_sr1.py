#!/usr/bin/env python3

from scapy.all import *

print("## Capa 2 - srp1")
#pkg1 = Ether()/IP(dst="google.com")/TCP(dport=80, flags="S")
pkg1 = Ether()/IP(dst="192.168.1.10")/TCP(dport=80, flags="S")
print(pkg1.show())
print(pkg1.summary())
ans1 = srp1(pkg1, verbose=0)
print(TCP in ans1)
print(ICMP in ans1)
print(ans1)
# Nota: desde local se manda un SYN y el target debe intentar devolver un SYNC, ACK

input("Presione cualquier tecla para continuar el reenvio...")

print("## Capa 2 - srp1 - sendp")
my_tcp = ans1[TCP] # Extraemos su layer TCP
print(my_tcp.show())
my_tcp.flasgs = "S"
#pkg1_1 = Ether()/IP(dst="google.com")/my_tcp
pkg1_1 = Ether()/IP(dst="192.168.1.10")/my_tcp
r2 = sendp(pkg1_1, iface="en0", verbose=0)
print(pkg1_1.show())
print(pkg1_1.summary())
print(r2)
# Nota: desde local se manda un SYN, ACK y el target debe intentar devolver un RST
