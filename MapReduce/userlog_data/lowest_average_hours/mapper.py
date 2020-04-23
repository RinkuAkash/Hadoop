#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    user_log=line.split(',')
    if user_log[4] != 'working_hours':
        print("%s,%s,%s" %(user_log[0], user_log[4], 1))
