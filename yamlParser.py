#!/usr/bin/env python
# encoding: UTF-8

import sys
import yaml

print(sys.argv[1])
print(open(sys.argv[1]))
print(yaml.load(open(sys.argv[1])))