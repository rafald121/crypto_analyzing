import json
import requests
import time
from utils import utils_string, utils_file

def get_json_from_url(url):
    _response = ''
    while _response == '':
        try:
            _response = requests.get(url)
        except:
            print("Connection refused by the server.. \n"
                  "Let me sleep for 2 seconds")
            time.sleep(2)
            failed_coin = utils_string.get_from_coin_from_url(url)
            utils_file.add_coin_to_file(failed_coin + '\n')
            print("Added {} to file with failed coin".format(failed_coin))
            print("Error for url: {}".format(url))
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