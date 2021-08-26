#!/usr/bin/env python

import sys

from lib.convert import bin_dec
from lib.mask import get_mask

my_prefix = int(sys.argv[1])
my_mask = get_mask(my_prefix)
print(".".join(my_mask))

n = 32 - my_prefix
print("n:", n)

ips = (2**n)-2
print("ips:", ips)
