import time
from json_methods.json_base import get_json_from_url, get_json_array_by_attr
from utils.utils_date_time import get_limit_from_datefrom, get_seconds_from_interval_symbol, \
    get_fullname_from_interval_symbol, get_epoch_from_date
from utils.utils_date_time import get_curr_epoch, get_date_from_epoch

COIN_FROM = "BTC"
COIN_TO = "USD"
LIMIT = 5
INTERVAL_ARRAY = {'M': 'histominute',
                  'H': 'histohour',
                  'D': 'histoday',}

INTERVAL_SECONDS = {'M': 60,
                   'H': 3600,
                   'D': 86400}

CURRENT_EPOCH = round(time.time())

class Historical_Data:
    DEFAULT_COIN_FROM = 'BTC'
    DEFAULT_COIN_TO = 'USD'
    DEFAULT_DATE_FROM = "2017.08.01 14:20:00"
    DEFAULT_DATE_TO = get_curr_epoch()
    DEFAULT_LIMIT = 100
    DEFAULT_INTERVAL = 'D'
    date_from = DEFAULT_DATE_FROM,






    historical_json_data = None

    def __init__(self,
                 date_from  = DEFAULT_DATE_FROM,
                 date_to    = CURRENT_EPOCH,
                 coin_from  = DEFAULT_COIN_FROM,
                 coin_to    = DEFAULT_COIN_TO,
                 limit     = DEFAULT_LIMIT,
                 interval   = DEFAULT_INTERVAL):
        self._date_from = date_from
        self._date_to   = date_to,
        self._coin_from = coin_from,
        self._coin_to   = coin_to,
        self._limit     = limit,
        self._interval  = interval

        self.historical_json_data = self.get_historical_data(date_from,date_to,coin_from,coin_to,limit,interval)

    def get_historical_data(self,
                            date_from  = DEFAULT_DATE_FROM,
                            date_to    = CURRENT_EPOCH,
                            coin_from  = DEFAULT_COIN_FROM,
                            coin_to    = DEFAULT_COIN_TO,
                            limit      = DEFAULT_LIMIT,
                            interval   = DEFAULT_INTERVAL):
        interval_str = get_fullname_from_interval_symbol(interval)
        if type(date_to) is str:
            date_to = get_epoch_from_date(date_to)

        if date_from == None:
            if limit == None:
                _limit = 1000
            else:
                _limit=limit
        else:
            interval_seconds = get_seconds_from_interval_symbol(interval)
            _limit = get_limit_from_datefrom(date_from, date_to, interval=interval_seconds)
        URL = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit={}&aggregate=1&toTs={}"\
            .format(interval_str, coin_from, coin_to, _limit, date_to)
        json_content = get_json_from_url(URL)
        json_data = get_json_array_by_attr(json_content, 'Data')
        return json_data

    def get_object_configuration(self):
        print(self.date_from)
        return ("*OBJECT CONFIGURATION* \n"
                "Coin from: {} \ncoin to: {} \ndate from: {} \ndate to: {} \ninterval: {} \nlimit: {} \n"
            .format(
            self._coin_from[0],
            self._coin_to[0],
            self._date_from,
            get_date_from_epoch(self._date_to[0]),
            self._interval[0],
            self._limit[0]))

#
#
# btc_historical = Historical_Data(date_from="2016.09.04 12:00:00")
# print(btc_historical.get_object_configuration())
#
#
#
