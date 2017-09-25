from utils.utils_date_time import get_curr_epoch, get_date_from_epoch,DATE_FORMAT

def print_curr_timestamp():
    print (get_curr_epoch())

def print_data(json_data):
    for interval in json_data:
        print_interval(interval)

def print_interval(interval):
    print("for date: {}".format(get_date_from_epoch(interval['time'])))
    for attr in interval:
        print("{}: {}".format(attr, interval[attr]))

def print_date_array_from_epochs(array):
    for i in array:
        print(get_date_from_epoch(i,format=DATE_FORMAT))

