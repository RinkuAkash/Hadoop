#!/usr/bin/env python3

"""Mapper code to check survived persons traveling class wise"""

import sys


for line in sys.stdin:
    passenger_info = line.split(',')
    if passenger_info[1] == '0':
        print("%s,%s" % (passenger_info[2], 1))

