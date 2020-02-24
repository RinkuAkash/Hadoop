REGISTER '/home/hduser/Desktop/Hadoop/Pig/udfs/python_functions.py' USING streaming_python  as py_functions;

data = LOAD '/home/hduser/Desktop/Hadoop/Pig/udfs/user_log_data.csv'
USING PigStorage(',') AS (user_name:chararray, end_time:chararray,
idle_time:chararray, start_time:chararray, working_hours:chararray);

users = FOREACH data GENERATE py_functions.get_user_name(user_name), py_functions.get_idle_time(idle_time);

sorted_users = ORDER users BY idle_time DESC;

idle_hours = LIMIT sorted_users 10;

top_idle_hours = FOREACH idle_hours GENERATE $0;

DUMP top_idle_hours;

