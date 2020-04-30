#!/usr/bin/env python3

import sys
import yaml

file_param = sys.argv[1]

with open(file_param, 'r') as input_file:
  tosca = yaml.load(input_file, Loader=yaml.FullLoader)

del tosca['topology_template']['policies']

with open(file_param, 'w') as output_file:
  yaml.dump(tosca, output_file)



