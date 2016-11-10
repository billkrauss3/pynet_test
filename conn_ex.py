#! /usr/bin/env python

from net_system.models import NetworkDevice, Credentials
import django
import threading
import Queue
import pprint
import os
import subprocess

#===============================================================================================
def db_lookup(device_name,my_queue):
  result = {}
  device = NetworkDevice.objects.get(device_name=device_name)
  result['name'] = device.device_name 
  result['vendor'] = device.vendor 
  result['type'] = device.device_type
  psef = subprocess.Popen(['/bin/ps','-ef'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  (std_out, std_err) = psef.communicate()
  result['ps'] = std_out

  # pprint.pprint(result)
  my_queue.put(result) 

#===============================================================================================

def main():
  django.setup()
  my_queue = Queue.Queue()
  devices = NetworkDevice.objects.all()
  for device in devices:
    my_thread = threading.Thread(target=db_lookup, args=(device.device_name,my_queue))
    my_thread.start()
  
  main_thread = threading.currentThread()
  for some_thread in threading.enumerate():
    if some_thread != main_thread:
      some_thread.join()
  
  while not my_queue.empty():
    result = my_queue.get()
    print result['name'], result['vendor'], result['type'], result['ps']

if __name__ == "__main__":
  main()
