#!/usr/bin/env python3


import sys

for line in sys.stdin:
    user_log = line.split(',')
    if user_log[3] > '2019-10-24 09:30:00' and user_log[3] != 'start_time':
        print("%s, %s, %s" %(user_log[0], user_log[3], 1))
