from pig_util import outputSchema
import datetime


@outputSchema('user_name:chararray')
def get_user_name(user_name):
    return user_name

@outputSchema('start_time:chararray')
def get_start_time(start_time):
    return start_time

@outputSchema('idle_time:chararray')
def get_idle_time(idle_time):
    return idle_time

@outputSchema('average_seconds:int')
def get_working_hours(working_hours):
    actual_time = datetime.datetime.strptime(working_hours, '%Y-%m-%d %H:%M:%S')
    total_seconds = actual_time.hour * 3600 + actual_time.minute * 60 + actual_time.second
    return int(total_seconds)
