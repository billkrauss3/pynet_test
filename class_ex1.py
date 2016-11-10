#!/usr/bin/env python

import re
import pprint

class ShowVer(object):
  def __init__(self,filename):
    self.filename = filename
    f = open(filename,"r")
    self.data = {}
    self.show_ver = f.read()
    # print self.show_ver
    result = self.OSVersion(self)
    self.data['OS Version'] = result
    result = self.Vendor(self)
    self.data['Vendor'] = result
    result = self.Model(self)
    self.data['Model'] = result
    result = self.SerialNumber(self)
    self.data['Serial Number'] = result
    result = self.Uptime(self)
    self.data['Uptime'] = result

  def PrintAll(self):
    for key in self.data:
      print "  {}: {}".format(key,self.data[key])
    return self.data
  
  def Vendor(self,show_ver):
    result = re.search(r"^(.*?), ", self.show_ver)
    return result.group(1)
  
  def OSVersion(self,show_ver):
    result = re.search(r"Version (.*?), ", self.show_ver)
    return result.group(1)
  
  def Model(self,show_ver):
    result = re.search(r"(.*) processor ", self.show_ver)
    return result.group(1)
  
  def SerialNumber(self,show_ver):
    result = re.search(r"Processor board ID (.*)", self.show_ver)
    return result.group(1)
  
  def Uptime(self,show_ver):
    result = re.search(r"uptime is (.*)", self.show_ver)
    return result.group(1)

test1 = ShowVer("show_version.txt")
data = test1.PrintAll()
pprint.pprint(data)

OS = test1.OSVersion()
print OS

# PrintDict(data)
# pprint.pprint(data)
