#! /usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

pynet_rtr1 = {
  'device_type': 'cisco_ios',
  'ip':   '184.105.247.70',
  'username': 'pyclass',
  'password': getpass(), }

pynet_sw1 = {
  'device_type': 'arista_eos',
  'ip':   '184.105.247.72',
  'username': 'pyclass',
  'password': getpass(), }

def GetDevInfo(devcred):
  # Connect
  net_connect = ConnectHandler(**devcred)
  
  # Show Prompts
  print "==========================================================================="
  print "Prompt: {}".format(net_connect.find_prompt())
  
  # Show int
  print "==========================================================================="
  output = net_connect.send_command("show ip int brief")
  print output
  
  # Show version
  print "==========================================================================="
  output = net_connect.send_command("show version")
  print output
  
  # Show run
  print "==========================================================================="
  output = net_connect.send_command("show run")
  print output
  runfilename = "running-config-" + devcred['ip']
  f = open(runfilename,"w")
  f.write(output)

for devcred in (pynet_rtr1, pynet_sw1):
  GetDevInfo(devcred)

