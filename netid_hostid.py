#!/usr/bin/env python

import sys

from lib.clase import get_clase
from lib.rango import get_rango
from lib.net_host import get_net_host


my_ip = sys.argv[1]
clase = get_clase(my_ip)

print("clase:", clase)

net_id, host_id = get_net_host(my_ip, clase)

rango = [None, None]
if clase!="D" and clase!="E":
    rango = get_rango(net_id)

print("net_id: %s - host_id: %s" % (net_id, host_id))
print("rango: %s - %s" % (rango[0], rango[1]))
