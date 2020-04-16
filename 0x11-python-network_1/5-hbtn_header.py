#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import requests
from sys import argv as args


if __name__ == "__main__":
    r = requests.get(args[1])
    print(r.headers.get('x-request-id'))
