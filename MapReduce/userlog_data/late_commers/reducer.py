#!/usr/bin/env python3


import sys


late_commers =0
for line in sys.stdin:
    username, start_time, count = line.split(',')
    late_commers+=int(count)
    print(username, start_time)

print("Total number of late commers are : %d" %late_commers)
