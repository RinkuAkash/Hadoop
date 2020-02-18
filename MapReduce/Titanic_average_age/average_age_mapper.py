#!/usr/bin/env python3

""" Mapper code to find average age of the people who died"""

import sys


for line in sys.stdin:
    passenger_info = line.split(',')
    if passenger_info[1] == '1':
        age = float(passenger_info[5])
        print("%s,%s" % (passenger_info[4], age))

