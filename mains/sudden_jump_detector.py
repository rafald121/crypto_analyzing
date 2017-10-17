from mains.historical_data import Historical_Data
from mains import coin_list
from utils import utils_date_time, utils_print, utils_sudden_jumps

class Sudden_jump_detector:
    DEFAULT_COIN_ARRAY = ['BTC','LTC','DMD','LSK']
    DEFAULT_COIN_TO = 'USD'
    DEFAULT_DATE_FROM = "2017.08.01 14:20:00"
    DEFAULT_DATE_TO = utils_date_time.get_curr_epoch()
    DEFAULT_INTERVAL = 'D'
    DEFAULT_THRESHOLD = 2.0

    sudden_jump_dict = {}
    sorted_list = []

    def __init__(self,
                 coin_array =DEFAULT_COIN_ARRAY,
                 coin_to    =DEFAULT_COIN_TO,
                 date_from  =DEFAULT_DATE_FROM,
                 date_to    =DEFAULT_DATE_TO,
                 interval   =DEFAULT_INTERVAL,
                 threshold  =DEFAULT_THRESHOLD
                 ):
        self._coin_array = coin_array,
        self._coin_to = coin_to,
        self._date_from = date_from,
        self._date_to = date_to,
        self._interval = interval,
        self._threshold = threshold

        self.sudden_jump_dict = self.get_suddent_jump_results(coin_array,coin_to,date_from,date_to,interval,threshold)
        self.sorted_list = utils_sudden_jumps.sort_dict_results_by_amount_of_occcurs_with_ratio(self.sudden_jump_dict)

    def get_sudden_jump(self,high_low_ratio_dict, threshold=DEFAULT_THRESHOLD):
        sudden_jumps = []
        for interval in high_low_ratio_dict:
            if float(high_low_ratio_dict[interval]) > float(threshold):
                sudden_jumps.append(interval)
        return sudden_jumps

    def get_sudden_jump_with_ratio(self,high_low_ratio_dict, threshold=DEFAULT_THRESHOLD):
        sudden_jumps_array = []
        for interval in high_low_ratio_dict:
            if float(high_low_ratio_dict[interval]) > float(threshold):
                ratio = high_low_ratio_dict[interval]
                sudden_jumps_array.append([interval,ratio])
        return sudden_jumps_array

    def get_suddent_jump_results(self,
                                 coin_array =DEFAULT_COIN_ARRAY,
                                 coin_to    =DEFAULT_COIN_TO,
                                 date_from  =DEFAULT_DATE_FROM,
                                 date_to    =DEFAULT_DATE_TO,
                                 interval   =DEFAULT_INTERVAL,
                                 threshold  =DEFAULT_THRESHOLD):
        sudden_jump_dict = {}
        for coin in coin_array:
            print("COMPUTING FOR COIN: {}".format(coin))
            coin_historical_data = Historical_Data(
                    date_from=date_from,
                    date_to=date_to,
                    coin_from=coin,
                    coin_to=coin_to,
                    interval=interval)
            high_low_ratio_dict = utils_sudden_jumps.get_dict_of_ratio_high_low(coin_historical_data.historical_json_data)
            sudden_jump_dict[coin] = self.get_sudden_jump_with_ratio(high_low_ratio_dict, threshold)
        return sudden_jump_dict

    def print_results(self, print_ratio = True):
        utils_print.print_sorted_list(self.sorted_list, self.sudden_jump_dict, print_ratio)

    def get_object_configuration(self):
        return("*OBJECT CONFIGURATION* \n"
            "Coin array: {} \ncoin to: {} \ndate from: {} \ndate to: {} \ninterval: {} \nthreshold: {} \n"
            .format(self._coin_array[0],
                    self._coin_to[0],
                    self._date_from[0],
                    self._date_to[0],
                    self._interval[0],
                    self._threshold))

list_bittrex = coin_list.get_cryptocurrency_list_bittrex_active()

object_sudden_jump_results = Sudden_jump_detector(
    coin_array  =list_bittrex,
    threshold   =2,
    date_from   ="2017.01.01 00:00:00",
    interval    ='H')

object_sudden_jump_results.print_results(print_ratio=True)

