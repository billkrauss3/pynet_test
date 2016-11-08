#!/usr/bin/env python

import re
import pprint

data ={} 

# Model Number
# OS version
# Serial number
# Uptime

def OpenShowVer(filename):
  f = open(filename,"r")
  show_ver = f.read()
  return show_ver

def PrintDict(dict):
  for key in dict:
    print "  {}: {}".format(key,dict[key])

def Vendor(show_ver):
  result = re.search(r"^(.*?), ", show_ver)
  return result.group(1)

def OSVersion(show_ver):
  result = re.search(r"Version (.*?), ", show_ver)
  return result.group(1)

def Model(show_ver):
  result = re.search(r"(.*) processor ", show_ver)
  return result.group(1)

def SerialNumber(show_ver):
  result = re.search(r"Processor board ID (.*)", show_ver)
  return result.group(1)

def Uptime(show_ver):
  result = re.search(r"uptime is (.*)", show_ver)
  return result.group(1)

show_ver = OpenShowVer("show_version.txt")
# print show_ver
result = OSVersion(show_ver)
data['OS Version'] = result

result = Vendor(show_ver)
data['Vendor'] = result

result = Model(show_ver)
data['Model'] = result

result = SerialNumber(show_ver)
data['Serial Number'] = result

result = Uptime(show_ver)
data['Uptime'] = result

PrintDict(data)
pprint.pprint(data)
