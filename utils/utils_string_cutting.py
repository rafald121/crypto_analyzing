
URL_to_cut = "https://min-api.cryptocompare.com/data/histoday?fsym=DASH&tsym=USD&limit=158&aggregate=1&toTs=1506344834&extraParams=your_app_name"
urxl = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=158&aggregate=1&toTs=1506345417&extraParams=your_app_name"

def get_from_coin_from_url(url):
    first_split = url.split('?')
    second_split = first_split[1].split('&')
    for p in second_split:
        if 'fsym' in p:
            return p.split('=')[1]

