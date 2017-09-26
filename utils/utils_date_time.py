import time

CURRENT_EPOCH = round(time.time())
DATE_FORMAT_TIME = '%Y.%m.%d %H:%M:%S'
DATE_FORMAT = '%Y.%m.%d'

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

def get_limit_from_dates(date_from, date_to = get_curr_epoch(), interval=INTERVAL_SECONDS['D']):
    epoch_from = get_epoch_from_date(date_from)
    if type(date_to) == str:
        epoch_to = get_epoch_from_date(date_to)
    elif type(date_to) == int:
        epoch_to = date_to
    else:
        print("ERROR WHILE CONVERTING DATES TO LIMIT")
        return -1
    limit = round((epoch_to-epoch_from)/interval)
    return limit

def get_seconds_from_interval_symbol(symbol):
    return INTERVAL_SECONDS[symbol]

def get_fullname_from_interval_symbol(symbol):
    return INTERVAL_ARRAY[symbol]
