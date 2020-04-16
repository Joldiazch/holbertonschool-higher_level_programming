#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import requests
from sys import argv as args


if __name__ == "__main__":
    URL = args[1]
    email = args[2]
    DATA = {
        'email': email
    }
    r = requests.post(url=URL, data=DATA)
    print(r.text)
