#!/usr/bin/env python

ip_addr = '192.168.1.1'
octets = ip_addr.split(".")

print "Before modification {}".format(octets)

octets[3] = '0'

print "After modification {}".format(octets)

for i,oct in enumerate(octets):
  print "Oct: {}, Decimal: {:3}, Binary: {:10}, Hex: {}".format((i+1),oct,bin(int(oct)),hex(int(oct)))
