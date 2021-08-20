#!/usr/bin/env python3

import sys
from scapy.all import *

src_mac = sys.argv[1]
src_ip = sys.argv[2]
dst_ip = sys.argv[3]

#ip = IP(src="127.1.2.3", dst="192.168.1.10", ttl=128, tos=9)
#ip = IP(src=sys.argv[1], dst="192.168.1.10", ttl=128, tos=9)
#ip = Ether()/IP(src=sys.argv[1], dst="192.168.1.10", ttl=128, tos=9)
#ip = Ether(src="0:e0:4c:f1:ce:a2")/IP(src=sys.argv[1], dst="192.168.1.10", ttl=128, tos=9)
ip = Ether(src=src_mac)/IP(src=src_ip, dst=dst_ip, ttl=128, tos=9)

# Prefijos
# “X (Ej: XByteField): Hace referencia a que se visualizará y tendrá formato hexadecimal: 0x05.
# LE: El tipo de dato está en representación Litte Endian. Por defecto es Big Endian. 
# S: Es un número con signo. Por defecto no tienen signo.

# ip.tos = 0xA

# sin procesar
#print(ip.show())

# simula procesado
print(ip.show2())

"""
“IP: https://www.ietf.org/rfc/rfc791.txt 
TCP: https://tools.ietf.org/rfc/rfc793.txt 
UDP: https://www.ietf.org/rfc/rfc768.txt 
ICMP: https://tools.ietf.org/rfc/rfc792.txt  
ARP: https://tools.ietf.org/rfc/rfc826.txt”
"""

# send solo para IP
#print(send(ip/ICMP()/"hello xD"))

# cuando se necesita Ether
print(sendp(ip/ICMP()/"hello from scapy"))

