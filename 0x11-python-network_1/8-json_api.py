#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import requests
from sys import argv as args


if __name__ == "__main__":
    URL = 'http://0.0.0.0:5000/search_user'
    q = ""
    if (len(args) == 2):
        q = args[1]
    DATA = {'q': q}
    r = requests.post(url=URL, data=DATA)
    try:
        json_dict = r.json()
        msg = "No result"
        if json_dict:
            msg = '[{}] {}'.format(json_dict['id'], json_dict['name'])
        print(msg)
    except ValueError:
        print("Not a valid JSON")
