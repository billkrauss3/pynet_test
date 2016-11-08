#!/usr/bin/env python

import re

f = open("show_ip_bgp.txt","r")
show_bgp = f.read()

header_lines, bgp_table = show_bgp.split("Weight Path");
# print bgp_table

line_list= bgp_table.split("\n")
for line in line_list:
  # print "=================================================================="
  # print line
  fields = line.split()
  if len(fields) < 2:
    continue
  # print fields
  as_path = " ".join(fields[5:-1])
  print "{:<19} {}".format(fields[1],as_path)
