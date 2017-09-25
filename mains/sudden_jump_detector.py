from mains.historical_data import get_historical_data
from mains.coin_list import get_coin_names_array, get_cryptocurrency_list_bittrex
from utils.utils_date_time import get_curr_epoch, get_date_from_epoch, DATE_FORMAT
from utils.utils_tables import print_readable_table
from utils.utils_print import print_date_array_from_epochs
from utils.utils_file import mark_end_of_failed_coin

DEFAULT_FROM_DATE = "2017.08.01 14:20:00"

def get_dict_of_ratio_open_close_candles(json_historical_data):
    open_close_ratio_dict = {}
    for interval in json_historical_data:
        if interval['low'] == 0:
            break
        ratio = float(interval['close'])/float(interval['open'])
        open_close_ratio_dict[interval['time']] = ratio
    return open_close_ratio_dict

def get_dict_of_ratio_high_low_candles(json_historical_data):
    high_low_ratio_dict = {}
    for interval in json_historical_data:
        if interval['low'] == 0:
            break
        ratio = float(interval['high'])/float(interval['low'])
        high_low_ratio_dict[interval['time']] = ratio
    return high_low_ratio_dict

def get_avarage_of_ratio(ratio_dict):
    if len(ratio_dict) == 0:
        return -1
    sum = 0
    for interval in ratio_dict:
        sum += abs(ratio_dict[interval])

    return sum/len(ratio_dict)

def get_sudden_jump(high_low_ratio_dict, threshold = 2.0):
    sudden_jumps = []
    for interval in high_low_ratio_dict:
        if float(high_low_ratio_dict[interval]) > float(threshold):
            sudden_jumps.append(interval)
    return sudden_jumps
# TODO sprawdzicc czy ta sama nazwa zmiennej tutaj \/ moze byc uzyta w wywolaniu nizej

def get_suddent_jump_results(coin_array,
                             _coin_to='USD',
                             _date_from=DEFAULT_FROM_DATE,
                             _date_to=get_curr_epoch(),
                             _interval='D',
                             _threshold = 2.0):
    sudden_jump_dict = {}
    for coin in coin_array:
        print("I M COUNTING FOR COIN: {}".format(coin))
        coin_historical_data = get_historical_data(coin_from=coin,
                                                   coin_to=_coin_to,
                                                   date_from=_date_from,
                                                   date_to=_date_to,
                                                   interval=_interval)
        open_close_ratio_dict = get_dict_of_ratio_open_close_candles(coin_historical_data)
        open_close_avg = get_avarage_of_ratio(open_close_ratio_dict)

        high_low_ratio_dict = get_dict_of_ratio_high_low_candles(coin_historical_data)
        high_low_avarage = get_avarage_of_ratio(high_low_ratio_dict)

        sudden_jump_dict[coin] = get_sudden_jump(high_low_ratio_dict, _threshold)
    print("end of counting")
    return sudden_jump_dict

def print_sudden_jump_results(sudden_jump_dict):
    for coin in sudden_jump_dict:
        if len(sudden_jump_dict[coin]) != 0:
            print("Coin: {} broke threshold {} times".format(coin, len(sudden_jump_dict[coin])))
            for epoch in sudden_jump_dict[coin]:
                print(get_date_from_epoch(epoch))
        else:
            print("{} didn't break threshold any time".format(coin))

def sort_dict_results_by_amount_of_occcurs(_dict):
    dict = _dict.copy()
    sorted_dict = []
    for i in range(0,len(dict)):
        most_occurs = 0
        most_occured_coin = None
        for coin in dict:
            if len(dict[coin]) == 0:
                continue
            elif len(dict[coin]) > most_occurs:
                most_occurs = len(dict[coin])
                most_occured_coin = coin

        if most_occured_coin != None:
            del dict[most_occured_coin]
            sorted_dict.append(most_occured_coin)

    return sorted_dict

def print_sorted_list(list, sudden_jump_dict):
    print("!!!!SORTED!!!!")
    print(list)
    for coin in list:
        print("{} with {} occurences: ".format(coin, len(sudden_jump_dict[coin])))
        print_date_array_from_epochs(sudden_jump_dict[coin])

def remove_bad_coin(list_whole, bad_coins):
    for coin in bad_coins:
        list_whole.remove(coin)
    return list_whole

FAILED_COIN = []
def add_coin_to_failed(coin):
    FAILED_COIN.append(coin)

list_bittrex = get_cryptocurrency_list_bittrex()

sudden_jump_dict = get_suddent_jump_results(list_bittrex, _threshold=2)

# print(sudden_jump_dict)
# print_sudden_jump_results(sudden_jump_dict)

mark_end_of_failed_coin()

sorted_list = sort_dict_results_by_amount_of_occcurs(sudden_jump_dict)
print_sorted_list(sorted_list, sudden_jump_dict)




