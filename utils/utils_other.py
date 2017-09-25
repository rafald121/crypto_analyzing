
def remove_bad_coin(list_whole, bad_coins):
    for coin in bad_coins:
        list_whole.remove(coin)
    return list_whole

FAILED_COIN = []

def add_coin_to_failed(coin):
    FAILED_COIN.append(coin)