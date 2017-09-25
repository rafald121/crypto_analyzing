from json_methods.json_base import get_json_from_url, get_json_array_by_attr

URL_COINLIST = "https://www.cryptocompare.com/api/data/coinlist/"
URL_COINLIST_BITTREX = "https://bittrex.com/api/v1.1/public/getcurrencies"
json_content = get_json_from_url(URL_COINLIST)
json_coin_dict = get_json_array_by_attr(json_content, 'Data')

def get_cryptocurrency_list():
    json_content = get_json_from_url(URL_COINLIST)
    return get_json_array_by_attr(json_content, 'Data')

def get_coin_names_array():
    COIN_LIST_NAMES = []
    for coin in json_coin_dict:
        COIN_LIST_NAMES.append(coin)
    return COIN_LIST_NAMES

def get_cryptocurrency_list_bittrex():
    json_content = get_json_from_url(URL_COINLIST_BITTREX)
    # print(json_content)
    json_list_of_crypto = get_json_array_by_attr(json_content, 'result')
    # print(json_list_of_crypto)
    COIN_LIST_NAMES = []
    for coin in json_list_of_crypto:
        COIN_LIST_NAMES.append(coin['Currency'])
    return COIN_LIST_NAMES

def get_cryptocurrency_dict_bittrex():
    json_content = get_json_from_url(URL_COINLIST_BITTREX)
    # print(json_content)
    json_list_of_crypto = get_json_array_by_attr(json_content, 'result')
    # print(json_list_of_crypto)
    COIN_DICT_NAMES = {}
    for coin in json_list_of_crypto:
        print(coin)
        COIN_DICT_NAMES[coin['Currency']] = coin['CurrencyLong']
    return COIN_DICT_NAMES
#
# coin_list_bittrex = get_cryptocurrency_list_bittrex()
# print(coin_list_bittrex)