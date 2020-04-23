#!/usr/bin/env python3

import sys
from time import mktime
from datetime import datetime

user_log = dict()
total_time = 0
total_users = 0

for line in sys.stdin:
    username, idle_time, count = line.split(',')
    total_users += int(count)
    idle_time = datetime.strptime(idle_time, '%Y-%m-%d %H:%M:%S')
    idle_timestamp = (idle_time.hour * 3600) + (idle_time.minute * 60) + idle_time.second
    total_time += idle_timestamp
    user_log[username] = idle_timestamp

average_time = total_time//total_users
highest_users = 0

for user in user_log.keys():
    if user_log.get(user) > average_time:
        highest_users += 1
        print(user)

print("Total number of highest idle hours users are: ", highest_users)
