#!/usr/bin/env python

ip_addr_list = [ '192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5' ]

print "Before modification {}".format(ip_addr_list)

ip_addr_list.append("192.168.1.6")
ip_addr_list.append("192.168.1.7")

print "After append {}".format(ip_addr_list)

first_popped = ip_addr_list.pop(0)
print "First Popped: {}".format(first_popped)
print "After Pop {}".format(ip_addr_list)

print "List Length: {}".format(len(ip_addr_list))

# reverse_sort = ip_addr_list.sort()
reverse_sort = sorted(ip_addr_list,reverse=True)

print "Reverse Sort {}".format(reverse_sort)

