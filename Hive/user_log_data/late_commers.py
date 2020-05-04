from pyhive import hive
import pandas as pd

# connection connects to hive server and uses database
connection = hive.connect(host='localhost', port=10000, database='user_log', auth='NOSASL')

# converting sql data to pandas dataframe
user_log_data = pd.read_sql('select * from user_log_data', connection)
# Removing unnecessary data
user_log_data = user_log_data.drop(user_log_data.index[0])
# Getting dataframe whose start time is above 9:30 AM
late_commers_data_filter = user_log_data[user_log_data['user_log_data.start_time'] > '2019-10-24 09:30:00']
# Getting user names only
late_commers = late_commers_data_filter['user_log_data.user_name']
print(late_commers)
connection.close()
