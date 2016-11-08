#! /usr/bin/env python

def my_func(x, y, z=20):
    val = x + y + z
    return val

retval = my_func(10,20,30)
print "retval={}".format(retval)

retval = my_func(y=10,x=20)
print "retval={}".format(retval)

# This will fail
# retval = my_func(y=10,x=20,30)
# print "retval={}".format(retval)

# This works
retval = my_func("bob","sue","ed")
print "retval={}".format(retval)

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

retval = my_func(list1,list2,list3)
print "retval={}".format(retval)
