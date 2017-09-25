import time

CURRENT_EPOCH = round(time.time())
DATE_FORMAT_TIME = '%Y.%d.%m %H:%M:%S'
DATE_FORMAT = '%m/%d/%Y'

INTERVAL_ARRAY = {'M': 'histominute',
                  'H': 'histohour',
                  'D': 'histoday',}

INTERVAL_SECONDS = {'M': 60,
                   'H': 3600,
                   'D': 86400}

def get_current_epoch():
    return round(time.time())

def get_curr_date():
    timeGMT = time.gmtime(CURRENT_EPOCH)
    curr_date = time.strftime(DATE_FORMAT_TIME, timeGMT)
    return ("Current date is: {}".format(curr_date))


def get_curr_epoch():
    return round(time.time())

def get_date_from_epoch(epoch, format=DATE_FORMAT_TIME):
    timeGMT = time.gmtime(epoch)
    curr_date = time.strftime(format, timeGMT)
    return curr_date

def get_epoch_from_date(date):
    return int(time.mktime(time.strptime(date, DATE_FORMAT_TIME)))

def get_limit_from_datefrom(date_from, date_to = get_curr_epoch(), interval='D'):
    epoch_from = get_epoch_from_date(date_from)
    epoch_to = date_to
    limit = round((epoch_to-epoch_from)/interval)
    return limit

def get_seconds_from_interval_symbol(symbol):
    return INTERVAL_SECONDS[symbol]

def get_fullname_from_interval_symbol(symbol):
    return INTERVAL_ARRAY[symbol]


# print("epoch: {}".format(convert_date_to_epoch("2017.21.09 12:00:00")))