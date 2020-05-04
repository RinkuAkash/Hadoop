from pyhive import hive
import pandas as pd

# connection connects to hive server and uses database
connection = hive.connect(host='localhost', port=10000, database='user_log', auth='NOSASL')

# converting sql data to pandas dataframe
user_log_data = pd.read_sql('select * from user_log_data', connection)
# Removing unnecessary data
user_log_data = user_log_data.drop(user_log_data.index[0])
# Converting string type of datetime to datetime format
user_log_data['user_log_data.idle_time'] = pd.to_datetime(user_log_data['user_log_data.idle_time'])
# Getting dataframe whose idle time is above average idle time
idle_hours_filter = user_log_data[user_log_data['user_log_data.idle_time'] > user_log_data['user_log_data.idle_time'].mean()]
# Getting user names only
highest_users = idle_hours_filter['user_log_data.user_name']

print(highest_users)
connection.close()
