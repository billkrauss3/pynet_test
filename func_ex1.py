#!/usr/bin/env python

def getfile(filename):
  # print "filename={}".format(filename)
  f = open(filename,"r")
  content = f.read()
  return content

def show_version(content):
  # print content
  for line in content.split("\n"):
    if "Processor board ID" in line:
      parts = line.split(" ")
      print "Serial Number: {}".format(parts[3])

content = getfile("show_version.txt")
show_version(content)
