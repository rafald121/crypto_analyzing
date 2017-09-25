def get_dict_of_ratio_open_close_candles(json_historical_data):
    open_close_ratio_dict = {}
    for interval in json_historical_data:
        if interval['low'] == 0:
            break
        ratio = float(interval['close'])/float(interval['open'])
        open_close_ratio_dict[interval['time']] = ratio
    return open_close_ratio_dict

def get_dict_of_ratio_high_low(json_historical_data):
    high_low_ratio_dict = {}
    for interval in json_historical_data:
        if interval['low'] == 0:
            break
        ratio = float(interval['high'])/float(interval['low'])
        high_low_ratio_dict[interval['time']] = ratio
    return high_low_ratio_dict

def get_avarage_of_ratio(ratio_dict):
    if len(ratio_dict) == 0:
        return -1
    sum = 0
    for interval in ratio_dict:
        sum += abs(ratio_dict[interval])

    return sum/len(ratio_dict)

def sort_dict_results_by_amount_of_occcurs(_dict):
    print('xD')
    print(_dict)
    dict = _dict.copy()
    sorted_dict = []
    for i in range(0,len(dict)):
        most_occurs = 0
        most_occured_coin = None
        for coin in dict:
            if len(dict[coin]) == 0:
                continue
            elif len(dict[coin]) > most_occurs:
                most_occurs = len(dict[coin])
                most_occured_coin = coin

        if most_occured_coin != None:
            del dict[most_occured_coin]
            sorted_dict.append(most_occured_coin)

    return sorted_dict

def sort_dict_results_by_amount_of_occcurs_with_ratio(_dict):
    print('xD')
    print(_dict)
    dict = _dict.copy()
    sorted_dict = []
    for i in range(0,len(dict)):
        most_occurs = 0
        most_occured_coin = None
        for coin in dict:
            if len(dict[coin]) == 0:
                continue
            elif len(dict[coin]) > most_occurs:
                most_occurs = len(dict[coin])
                most_occured_coin = coin

        if most_occured_coin != None:
            del dict[most_occured_coin]
            sorted_dict.append(most_occured_coin)

    return sorted_dict
