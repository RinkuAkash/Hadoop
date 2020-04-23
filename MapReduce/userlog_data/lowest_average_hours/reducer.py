#!/usr/bin/env python3

import sys
from datetime import datetime

user_log = dict()
total_time = 0
total_users = 0

for line in sys.stdin:
    username, working_time, count = line.split(',')
    total_users += int(count)
    working_time = datetime.strptime(working_time, '%Y-%m-%d %H:%M:%S')
    working_time_seconds = (working_time.hour * 3600) + (working_time.minute * 60) + working_time.second
    total_time += working_time_seconds
    user_log[username] = working_time_seconds

average_time = total_time//total_users
lowest_users = 0

for user in user_log.keys():
    if user_log.get(user) < average_time:
        lowest_users += 1
        print(user)

print("Total number of lowest average hours users are: ", lowest_users)
