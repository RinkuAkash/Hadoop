REGISTER '/home/hduser/Desktop/Hadoop/Pig/udfs/python_functions.py' USING streaming_python  as py_functions;

data = LOAD '/home/hduser/Desktop/Hadoop/Pig/udfs/user_log_data.csv'
USING PigStorage(',') AS (user_name:chararray, end_time:chararray,
idle_time:chararray, start_time:chararray, working_hours:chararray);

users = FOREACH data GENERATE py_functions.get_user_name(user_name), py_functions.get_start_time(start_time);

sorted_users = ORDER users BY start_time DESC;

late_commers = LIMIT sorted_users 10;

top_late_commers = FOREACH late_commers GENERATE $0;

DUMP top_late_commers;

