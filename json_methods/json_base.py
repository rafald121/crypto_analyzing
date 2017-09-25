import json
import requests
import time
# from mains.sudden_jump_detector import add_coin_to_failed
from utils.utils_string_cutting import get_from_coin_from_url
from utils.utils_file import add_coin_to_file


def get_json_from_url(url):
    print("url: {}".format(url))
    _response = ''
    while _response == '':
        try:
            _response = requests.get(url)
        # except requests.exceptions.RequestException as exc:
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")

            add_coin_to_file(get_from_coin_from_url(url) + '\n')

            print("eror for url: {}".format(url))
            continue
        else:
            response_content = _response.content
            json_response = json.loads(response_content)
            return json_response

def get_json_array_by_attr(json, attr):
    try:
        json_attr = json[attr]
    except ValueError:
        print("Decoding JSON has failed for json: {}".format(json))
    else:
        return json_attr