import time

def format_timestamp(timestamp):
	time_format = "%Y/%m/%d %H:%M:%S"
	return time.strftime(time_format, time.localtime(timestamp))
