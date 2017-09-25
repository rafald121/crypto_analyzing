from mains.historical_data import get_historical_data
from mains.coin_list import get_coin_names_array, get_cryptocurrency_list_bittrex
from utils.utils_date_time import get_curr_epoch, get_date_from_epoch, DATE_FORMAT
from utils.utils_tables import print_readable_table
from utils.utils_print import print_date_array_from_epochs, print_sudden_jump_results, print_sorted_list
from utils.utils_file import mark_end_of_failed_coin
from utils.utils_sudden_jumps import get_dict_of_ratio_high_low

class Sudden_jump_detector:
    DEFAULT_COIN_ARRAY = ['BTC','LTC','DMD','LSK']
    DEFAULT_COIN_TO = 'USD'
    DEFAULT_DATE_FROM = "2017.08.01 14:20:00"
    DEFAULT_DATE_TO = get_curr_epoch()
    DEFAULT_INTERVAL = 'D'
    DEFAULT_THRESHOLD = 2.0

    def __init__(self,
                 coin_array =DEFAULT_COIN_ARRAY,
                 coint_to   =DEFAULT_COIN_TO,
                 date_from  =DEFAULT_DATE_FROM,
                 date_to    =DEFAULT_DATE_TO,
                 interval   =
                 ):
        self.get_suddent_jump_results()

    def start(self):
        self.get_suddent_jump_results()

    def get_sudden_jump(self,high_low_ratio_dict, threshold=DEFAULT_THRESHOLD):
        sudden_jumps = []
        for interval in high_low_ratio_dict:
            if float(high_low_ratio_dict[interval]) > float(threshold):
                sudden_jumps.append(interval)
        return sudden_jumps

    def get_suddent_jump_results(self,
                                 _coin_array=   DEFAULT_COIN_ARRAY,
                                 _coin_to=      DEFAULT_COIN_TO,
                                 _date_from=    DEFAULT_DATE_FROM,
                                 _date_to=      DEFAULT_DATE_TO,
                                 _interval=     DEFAULT_INTERVAL,
                                 _threshold =   DEFAULT_THRESHOLD):
        sudden_jump_dict = {}
        for coin in _coin_array:
            print("COMPUTING FOR COIN: {}".format(coin))
            coin_historical_data = get_historical_data(coin_from=coin,
                                                       coin_to=_coin_to,
                                                       date_from=_date_from,
                                                       date_to=_date_to,
                                                       interval=_interval)
            high_low_ratio_dict = get_dict_of_ratio_high_low(coin_historical_data)
            sudden_jump_dict[coin] = self.get_sudden_jump(high_low_ratio_dict, _threshold)
        print("end of counting")
        return sudden_jump_dict

object1 = Sudden_jump_detector

list_bittrex = get_cryptocurrency_list_bittrex()

sudden_jump_dict = get_suddent_jump_results(list_bittrex, _threshold=2)

mark_end_of_failed_coin()

sorted_list = sort_dict_results_by_amount_of_occcurs(sudden_jump_dict)
print_sorted_list(sorted_list, sudden_jump_dict)




