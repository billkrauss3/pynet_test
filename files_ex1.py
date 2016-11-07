#!/usr/bin/env python

f = open("testdata.txt","r")
contents = f.read()
print contents

o = open("testoutput.txt","w")
o.write(contents)
o.close()

o = open("testoutput.txt","a")
o.write("Bytes, Bytes, Bytes")
o.close()
