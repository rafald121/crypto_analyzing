import json
import requests

def get_json_from_url(url):
    response = requests.get(url)
    response_content = response.content
    json_response = json.loads(response_content)
    return json_response

def get_json_array_by_attr(json, attr):
    return json[attr]