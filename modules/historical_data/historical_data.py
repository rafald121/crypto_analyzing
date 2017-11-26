from utils import utils_date_time
from utils import utils_tables
from utils import utils_json

URL_BASE = "https://min-api.cryptocompare.com/data/"

class Historical_Data:

    DEFAULT_COIN_FROM = 'BTC'
    DEFAULT_COIN_TO = 'USD'
    DEFAULT_DATE_FROM = "2017.08.01 14:20:00"
    DEFAULT_DATE_TO = utils_date_time.get_curr_epoch()
    DEFAULT_LIMIT = 100
    DEFAULT_INTERVAL = 'D'

    historical_json_data = None

    def __init__(self,
                 date_from  = DEFAULT_DATE_FROM,
                 date_to    = DEFAULT_DATE_TO,
                 coin_from  = DEFAULT_COIN_FROM,
                 coin_to    = DEFAULT_COIN_TO,
                 limit      = DEFAULT_LIMIT,
                 interval   = DEFAULT_INTERVAL):
        self._date_from = date_from
        self._date_to   = date_to,
        self._coin_from = coin_from,
        self._coin_to   = coin_to,
        self._limit     = limit,
        self._interval  = interval

        self.historical_json_data = self.get_historical_data(self,date_from,date_to,coin_from,coin_to,limit,interval)

    @staticmethod
    def get_historical_data(self,
                            date_from  = DEFAULT_DATE_FROM,
                            date_to    = DEFAULT_DATE_TO,
                            coin_from  = DEFAULT_COIN_FROM,
                            coin_to    = DEFAULT_COIN_TO,
                            limit      = DEFAULT_LIMIT,
                            interval   = DEFAULT_INTERVAL):
        interval_str = utils_date_time.get_fullname_from_interval_symbol(interval)

        date_to = self.get_date_to(date_to)
        _limit = self.get_date_from_from_limit(date_from, date_to, limit, interval)

        URL = URL_BASE + "{}?fsym={}&tsym={}&limit={}&aggregate=1&toTs={}"\
            .format(interval_str, coin_from, coin_to, _limit, date_to)

        json_content = utils_json.get_json_from_url(URL)
        json_data    = utils_json.get_json_array_by_attr(json_content, 'Data')
        return json_data

    def get_date_to(self, date_to):
        if type(date_to) is str:
            _date_to = utils_date_time.get_epoch_from_date(date_to)
            return _date_to
        elif type(date_to) is int:
            return date_to
        else:
            return None

    def get_date_from_from_limit(self, date_from, date_to, limit, interval):
        if date_from == None:
            if limit == None:
                _limit = 1000
            else:
                _limit = limit
        else:
            interval_seconds = utils_date_time.get_seconds_from_interval_symbol(interval)
            _limit = utils_date_time.get_limit_from_dates(date_from, date_to, interval=interval_seconds)
        return _limit

    def get_object_configuration(self):
        return ("*OBJECT CONFIGURATION* \n"
                "Coin from: {} \ncoin to: {} \ndate from: {} \ndate to: {} \ninterval: {} \nlimit: {} \n"
                .format(
                self._coin_from[0],
                self._coin_to[0],
                self._date_from,
                utils_date_time.get_date_from_epoch(self._date_to[0]),
                self._interval[0],
                self._limit[0]))

    def print_historical_data(self):
        utils_tables.print_readable_table(self.historical_json_data)

