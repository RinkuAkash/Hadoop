import os

command = "sqoop export --connect jdbc:mysql://localhost:3306/hadoopDB --username hduser --password hduser --table user_log --export-dir /user_log_data/user_log_data.csv"

os.system(command)
