import time
from json_methods.json_base import get_json_from_url, get_json_array_by_attr
from utils.utils_date_time import get_limit_from_datefrom, get_seconds_from_interval_symbol, \
    get_fullname_from_interval_symbol, get_epoch_from_date

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
    # URL = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit={}&aggregate=1&toTs={}&extraParams=your_app_name"\
    #     .format(interval_str, coin_from, coin_to, limit, date_to)
    URL = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit={}&aggregate=1&toTs={}"\
        .format(interval_str, coin_from, coin_to, limit, date_to)

    json_content = get_json_from_url(URL)
    json_data = get_json_array_by_attr(json_content, 'Data')
    return json_data

