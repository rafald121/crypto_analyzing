import json
import requests
import time


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