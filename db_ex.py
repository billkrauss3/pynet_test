#! /usr/bin/env python

from net_system.models import NetworkDevice, Credentials
import django
django.setup()

def EX1():
  print "=" * 100
  net_devices = NetworkDevice.objects.all()
  print net_devices
  
  print "=" * 100
  creds = Credentials.objects.all()
  print creds
  
  print "=" * 100
  for device in net_devices:
    print "Device: ", device, device.device_type, device.credentials
    if 'arista' in device.device_type:
      device.credentials = creds[1]
    else:
      device.credentials = creds[0]
    print "  ", device, device.credentials
    device.save()
  print "=" * 100

def EX2():
  print "=" * 100
  net_devices = NetworkDevice.objects.all()
  for device in net_devices:
    print "Device: ", device, device.device_type, device.vendor
    parts = device.device_type.split("_")
    device.vendor = parts[0]
    device.save()
    print "  ", device, device.vendor
  print "=" * 100

def EX3():
  pynet_rtr = NetworkDevice(
    device_name='pynet-rtr3',
    device_type='cisco_ios',
    ip_address='184.105.247.77',
    port=22,
    )
  pynet_rtr.save()

  pynet_sw = NetworkDevice.objects.get_or_create(
    device_name='pynet-sw5',
    device_type='arista_eos',
    ip_address='184.105.247.78',
    port=22,
    )

  net_devices = NetworkDevice.objects.all()
  print net_devices

def EX4():
  print "=" * 100
  device_list = ['pynet-rtr3','pynet-sw5']
  for device_name in device_list:
    print "Device Name: ", device_name
    try: 
      device = NetworkDevice.objects.get(device_name=device_name)
    except:
      print "  Device not found: ", device_name
      continue
    print "  ", device.device_name, device.device_type, device.ip_address
    device.delete()

  print "=" * 100
  net_devices = NetworkDevice.objects.all()
  for device in net_devices:
    print "  ", device.device_name, device.device_type, device.ip_address
  print "=" * 100

# EX1()
# EX2()
EX3()
EX4()
EX4()
