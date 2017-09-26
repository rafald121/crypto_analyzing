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

def print_interval_with_date(interval):
    print("{} : {}".format(get_date_from_epoch(interval['time']), interval))

def print_date_array_from_epochs(array):
    for i in array:
        print(get_date_from_epoch(i,format=DATE_FORMAT))

def print_occur_date_with_ratio(list):
    for i in list:
        print("Date: {}, ratio: {}".format(get_date_from_epoch(i[0],format=DATE_FORMAT),
                                            i[1]))

def print_sudden_jump_results(sudden_jump_dict):
    for coin in sudden_jump_dict:
        if len(sudden_jump_dict[coin]) != 0:
            print("Coin: {} broke threshold {} times".format(coin, len(sudden_jump_dict[coin])))
            for epoch in sudden_jump_dict[coin]:
                print(get_date_from_epoch(epoch))
        else:
            print("{} didn't break threshold any time".format(coin))

def print_sorted_list(list, sudden_jump_dict):
    print("!!!!SORTED!!!!")
    for coin in list:
        print("{} with {} occurences: ".format(coin, len(sudden_jump_dict[coin])))
        print_date_array_from_epochs(sudden_jump_dict[coin])

def print_sorted_list_with_ratio(list, sudden_jump_dict):
    print("!!!!SORTED RATIO!!!!")
    for coin in list:
        print("{} with {} occurences: ".format(coin, len(sudden_jump_dict[coin])))
        print_occur_date_with_ratio(sudden_jump_dict[coin])
        # print("Date: {}, ratio: {}".format(get_date_from_epoch(sudden_jump_dict[])))