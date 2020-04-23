#!/usr/bin/env python3

import sys

for line in sys.stdin:
    user_log=line.split(',')
    if user_log[2] != 'idle_time':
        print("%s,%s,%s" %(user_log[0], user_log[2], 1))
