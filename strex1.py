#!/usr/bin/env python

str_1 = "John Doe"
str_2 = "John Conner"
str_3 = "John Lennon"

print "{:>30} {:>30} {:>30}".format(str_1, str_2, str_3)
str_4 = raw_input("Enter fourth name: ")
print "{:>30}".format(str_4)
