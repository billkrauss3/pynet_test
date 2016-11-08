#! /usr/bin/env python

def my_func(x,y,z):
  print "x={}, y={}, z={}".format(x,y,z)
  sum = x + y + z
  return sum

list1 = [1,2,3]
dict1 = {
  'x': 5,
  'y': 10,
  'z': 15 }

retval = my_func(*list1)
print "retval={}".format(retval)

retval = my_func(**dict1)
print "retval={}".format(retval)
