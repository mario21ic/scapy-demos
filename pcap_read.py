#!/usr/bin/env python3

from scapy.all import *

pcap = rdpcap("send_sr1_pcap.pcap") # leer
#wcap = wdpcap("send_sr1_pcap.pcap") # escribir
print(pcap)

print("## Summary")
print(pcap.summary())

print("## Show")
print(pcap.show())

print("## Sessions")
print(len(pcap.sessions()))
#for x in pcap.sessions():
#    print("====")
#    print(x)

print("## Stats")
print(pcap.stats)

print("## TCP 80")
tcp_80 = {x:y for x,y in pcap.sessions().iteritems() if "TCP" in x and "80" in x}
print(tcp_80)
