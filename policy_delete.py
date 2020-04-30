#!/usr/bin/env python3

import glob
import os
import sys
import yaml

folder_param = sys.argv[1]

for file_param in glob.glob(folder_param + "/*.tosca"):
  with open(file_param, 'r') as input_file:
    tosca = yaml.load(input_file, Loader=yaml.FullLoader)

  if 'policy_types' in tosca:
    del tosca['policy_types']

  if 'topology_template' in tosca and  'policies' in tosca['topology_template']:
    del tosca['topology_template']['policies']

  with open(file_param, 'w') as output_file:
    yaml.dump(tosca, output_file)



