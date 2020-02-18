#!/usr/bin/env python3

"""Reducer program to find number of survived persons traveling class wise"""

import sys


passenger_info = dict()

for line in sys.stdin:
    passenger_class, count = line.split(',')
    try:
        passenger_info[passenger_class] = passenger_info[passenger_class]+int(count)
    except:
        passenger_info[passenger_class] = int(count)

for passenger_class in passenger_info.keys():
    print("%s : %d" % (passenger_class, passenger_info[passenger_class]))
