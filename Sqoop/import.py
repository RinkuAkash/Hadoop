import os

command = "sqoop import --connect jdbc:mysql://localhost:3306/hadoopDB --username hduser --password hduser --table user_log --m 1 --target-dir /userlog"

os.system(command)
