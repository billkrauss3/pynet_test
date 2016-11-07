#!/usr/bin/env python

num_list = range(1,50)

print "List: {}".format(num_list)

for i,num in enumerate(num_list):
  if num == 13:
    continue
  print "[{}] {}".format(i,num)
  if num == 39:
    break
