REGISTER '/home/hduser/Desktop/Hadoop/Pig/udfs/python_functions.py' USING streaming_python AS py_functions;

REGISTER '/home/hduser/pig-0.17.0/contrib/piggybank/java/piggybank.jar';

data = LOAD '/home/hduser/Desktop/Hadoop/Pig/udfs/user_log_data.csv' USING
 org.apache.pig.piggybank.storage.CSVExcelStorage(',', 'NO_MULTILINE', 'UNIX', 'SKIP_INPUT_HEADER')
 AS (user_name:chararray, end_time:chararray,
idle_time:chararray, start_time:chararray, working_hours:chararray);

users = FOREACH data GENERATE py_functions.get_user_name(user_name),
 py_functions.get_working_hours(working_hours);

users_group = GROUP users all;

average_value = FOREACH users_group GENERATE AVG(users.average_seconds) AS average;

group_average = CROSS users, average_value;

filtered_users = FILTER group_average BY (average_seconds > average);

highest_users = FOREACH filtered_users GENERATE user_name;

DUMP highest_users;


