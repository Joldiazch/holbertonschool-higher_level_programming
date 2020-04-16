#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import requests
from sys import argv as args


if __name__ == "__main__":
    URL = 'https://api.github.com/user'
    DATA = {'username': args[1], 'token': args[2]}
    r = requests.get(url=URL, auth=(DATA['username'], DATA['token']))
    try:
        json_dict = r.json()
        msg = "No result"
        if json_dict:
            msg = '{}'.format(json_dict['id'])
        print(msg)
    except ValueError:
        print("Not a valid JSON")
