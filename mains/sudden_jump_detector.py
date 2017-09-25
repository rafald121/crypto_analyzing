from mains.historical_data import get_historical_data
from mains.coin_list import get_coin_names_array, get_cryptocurrency_list_bittrex,get_cryptocurrency_active_list_bittrex
from utils.utils_date_time import get_curr_epoch, get_date_from_epoch, DATE_FORMAT
from utils.utils_tables import print_readable_table
from utils.utils_print import print_date_array_from_epochs, print_sudden_jump_results, print_sorted_list
from utils.utils_file import mark_end_of_failed_coin
from utils.utils_sudden_jumps import get_dict_of_ratio_high_low, sort_dict_results_by_amount_of_occcurs
class Sudden_jump_detector:
    DEFAULT_COIN_ARRAY = ['BTC','LTC','DMD','LSK']
    DEFAULT_COIN_TO = 'USD'
    DEFAULT_DATE_FROM = "2017.08.01 14:20:00"
    DEFAULT_DATE_TO = get_curr_epoch()
    DEFAULT_INTERVAL = 'D'
    DEFAULT_THRESHOLD = 2.0

    coin_array = DEFAULT_COIN_ARRAY,
    coin_to = DEFAULT_COIN_TO,
    date_from = DEFAULT_DATE_FROM,
    date_to = DEFAULT_DATE_TO,
    interval = DEFAULT_INTERVAL,
    threshold = DEFAULT_THRESHOLD

    sudden_jump_dict = {}
    sorted_list = []

    def __init__(self,
                 coin_array =DEFAULT_COIN_ARRAY,
                 coin_to   =DEFAULT_COIN_TO,
                 date_from  =DEFAULT_DATE_FROM,
                 date_to    =DEFAULT_DATE_TO,
                 interval   =DEFAULT_INTERVAL,
                 threshold  =DEFAULT_THRESHOLD
                 ):
        print("araj: {}".format(coin_array))
        self.sudden_jump_dict = self.get_suddent_jump_results(coin_array,coin_to,date_from,date_to,interval,threshold)
        self.sorted_list = sort_dict_results_by_amount_of_occcurs(self.sudden_jump_dict)
        self.print_results()
        print('end in da init')



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

    def print_results(self):
        print_sorted_list(self.sorted_list, self.sudden_jump_dict)

    def get_object_configuration(self):
        return("*OBJECT CONFIGURATION* \n"
               "Coin array: {} \ncoin to: {} \ndate from: {} \ndate to: {} \ninterval: {} \nthreshold: {} \n".format(self.coin_array,self.coin_to,self.date_from,self.date_to,self.interval,self.threshold))

list_bittrex = get_cryptocurrency_active_list_bittrex()[:10]

object_sudden_jump_results = Sudden_jump_detector(coin_array=list_bittrex, threshold=2)
object_sudden_jump_results.print_results()
# print(object_sudden_jump_results.get_object_configuration())
# print(object_sudden_jump_results.coint_aray)
# mark_end_of_failed_coin()

# print_sorted_list(sorted_list, object_sudden_jump_results.sudden_jump_dict)




