from pyhive import hive
import pandas as pd

# connection connects to hive server and uses database
connection = hive.connect(host='localhost', port=10000, database='user_log', auth='NOSASL')

# converting sql data to pandas dataframe
user_log_data = pd.read_sql('select user_name, working_time from user_log_data', connection)
# Removing unnecessary data
user_log_data = user_log_data.drop(user_log_data.index[0])
# Converting string type of datetime to datetime format
user_log_data['working_time'] = pd.to_datetime(user_log_data['working_time'])
# Getting dataframe whose working hour is below average working hours
working_hours_filter = user_log_data[user_log_data['working_time'] < user_log_data['working_time'].mean()]
# Getting user names only
lowest_users = working_hours_filter['user_name']

print(lowest_users)
connection.close()
