#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import requests
from sys import argv as args


if __name__ == "__main__":
    URL = args[1]
    r = requests.get(url=URL)
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
