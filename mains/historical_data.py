import time

from json_methods.json_base import get_json_from_url, get_json_array_by_attr
from utils.utils_date_time import get_limit_from_datefrom, get_seconds_from_interval_symbol, \
    get_fullname_from_interval_symbol, get_epoch_from_date
from utils.utils_tables import create_readable_table_from_jsonarray, print_readable_table
# from utils import utils_date_time

COIN_FROM = "BTC"
COIN_TO = "USD"
LIMIT = 5
INTERVAL_ARRAY = {'M': 'histominute',
                  'H': 'histohour',
                  'D': 'histoday',}

INTERVAL_SECONDS = {'M': 60,
                   'H': 3600,
                   'D': 86400}

# INTERVAL = INTERVAL_ARRAY['M']
CURRENT_EPOCH = round(time.time())
# URL_PARAMETERS = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit={}&aggregate=1&toTs={}&extraParams=your_app_name"\
#     .format(INTERVAL, COIN_FROM, COIN_TO, LIMIT, CURRENT_EPOCH)


def get_historical_data(date_from,
                        date_to = CURRENT_EPOCH,
                        coin_from = "BTC",
                        coin_to="USD",
                        _limit = 100,
                        interval = "H"):
    interval_str = get_fullname_from_interval_symbol(interval)
    if type(date_to) is str:
        date_to = get_epoch_from_date(date_to)

    if date_from == None:
        if _limit == None:
            limit = 1000
        else:
            limit=_limit
    else:
        interval_seconds = get_seconds_from_interval_symbol(interval)
        limit = get_limit_from_datefrom(date_from, date_to, interval=interval_seconds)
    # print("limit is: {}".format(limit))
    URL = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit={}&aggregate=1&toTs={}&extraParams=your_app_name"\
        .format(interval_str, coin_from, coin_to, limit, date_to)
    # print(URL)
    json_content = get_json_from_url(URL)
    json_data = get_json_array_by_attr(json_content, 'Data')
    return json_data


# limit = get_limit_from_datefrom(date_from="2016.20.09 12:30:00", interval=INTERVAL_SECONDS['M'])

# BTC_historical_data = get_historical_data(date_from="2016.04.04 12:30:00",date_to="2017.09.01 12:00:00")
# BTC_readabletable = create_readable_table_from_jsonarray(BTC_historical_data,format=DATE_FORMAT_TIME)
# print(BTC_historical_data)
# print(BTC_readabletable)
# # print(limit)

CLOAK_data = get_historical_data(date_from='2017.01.09 12:00:00', coin_from='BCC', coin_to='BTC', date_to='2017.30.09 12:00:00',interval='D')
# # cloak_readable = create_readable_table_from_jsonarray(CLOAK_data)
print_readable_table(CLOAK_data)