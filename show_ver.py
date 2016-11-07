#!/usr/bin/env python

f = open("show_version.txt","r")
for line in f:
  if "Processor board ID" in line:
    # print "> {}".format(line)
    parts = line.split(" ")
    print "Serial Number: {}".format(parts[3])
