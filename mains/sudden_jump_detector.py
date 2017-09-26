from mains.historical_data import Historical_Data
from mains.coin_list import get_coin_names_array, get_cryptocurrency_list_bittrex,get_cryptocurrency_active_list_bittrex
from utils.utils_date_time import get_curr_epoch, get_date_from_epoch, DATE_FORMAT
from utils.utils_tables import print_readable_table
from utils.utils_print import print_date_array_from_epochs, print_sudden_jump_results, print_sorted_list,print_sorted_list_with_ratio
from utils.utils_file import mark_end_of_failed_coin
from utils.utils_sudden_jumps import get_dict_of_ratio_high_low, sort_dict_results_by_amount_of_occcurs, sort_dict_results_by_amount_of_occcurs_with_ratio
# TABLIE KILKUWYMIAROWE TO BAZY DANYCH - moze z nich korzystac ?
# ANT with 1 occurences:
# Date: 2017.09.04, ratio: 10.06838905775076
#  przyklad że jak liczy higl/low na swiecy spadkowej to cos przekreca
class Sudden_jump_detector:
    DEFAULT_COIN_ARRAY = ['BTC','LTC','DMD','LSK']
    DEFAULT_COIN_TO = 'USD'
    DEFAULT_DATE_FROM = "2017.08.01 14:20:00"
    DEFAULT_DATE_TO = get_curr_epoch()
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
        # self.sorted_list = sort_dict_results_by_amount_of_occcurs(self.sudden_jump_dict)
        self.sorted_list = sort_dict_results_by_amount_of_occcurs_with_ratio(self.sudden_jump_dict)
        self.print_results_with_ratio()

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
        sudden_jump_dict_with_ratio = {}
        for coin in coin_array:
            print("COMPUTING FOR COIN: {}".format(coin))
            coin_historical_data = Historical_Data.get_historical_data(self,
                coin_from=coin,
                coin_to=coin_to,
                date_from=date_from,
                date_to=date_to,
                interval=interval)
            high_low_ratio_dict = get_dict_of_ratio_high_low(coin_historical_data)
            # sudden_jump_dict[coin] = self.get_sudden_jump(high_low_ratio_dict, threshold)
            sudden_jump_dict_with_ratio[coin] = self.get_sudden_jump_with_ratio(high_low_ratio_dict, threshold)
        return sudden_jump_dict_with_ratio



    # def print_results(self):
    #     print_sorted_list(self.sorted_list, self.sudden_jump_dict)
    def print_results_with_ratio(self):
        print_sorted_list_with_ratio(self.sorted_list, self.sudden_jump_dict)


    def get_object_configuration(self):
        return("*OBJECT CONFIGURATION* \n"
            "Coin array: {} \ncoin to: {} \ndate from: {} \ndate to: {} \ninterval: {} \nthreshold: {} \n"
            .format(
            self._coin_array[0],
            self._coin_to[0],
            self._date_from[0],
            get_date_from_epoch(self._date_to[0]),
            str(self._interval[0]),
            self._threshold))

    

list_bittrex = get_cryptocurrency_active_list_bittrex()

object_sudden_jump_results = Sudden_jump_detector(
    coin_array=['DMD'],
    threshold=1.5,
    date_from="2017.05.01 13:00:00")





