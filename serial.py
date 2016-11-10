#! /usr/bin/env python

import pprint
import json
import yaml

def GenData():
  data = ['First','Second','Third']
  moredata = {
    'x': 1,
    'y': 2,
    'z': 3 }
  data.append(moredata)
  data.append(True)
  return data

# Generate Data Structure
print "=" * 80
data = GenData()
print "Python: {}".format(data)

# Generate JSON 
print "=" * 80
json_obj = json.dumps(data)
print "JSON: " + json_obj
f = open("serial-data.json","w")
f.write(json_obj)
f.close()

f = file("serial-data.json","r")
json_obj_new = json.load(f)
print "JSON (new): " ,
pprint.pprint(json_obj_new)

print "json_obj_new[3]['y'] = {}".format(json_obj_new[3]['y'])

# Generate YAML
print "=" * 80
yaml_obj = yaml.dump(data)
print "YAML: " + yaml_obj
f = open("serial-data.yaml","w")
f.write(yaml_obj)
f.close()

f = file("serial-data.yaml","r")
yaml_obj_new = yaml.load(f)
print "YAML (new): ",
pprint.pprint(yaml_obj_new)

print "yaml_obj_new[3]['y'] = {}".format(yaml_obj_new[3]['y'])

print "=" * 80
