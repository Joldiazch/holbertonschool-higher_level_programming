#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import urllib.request
from sys import argv as args

if __name__ == "__main__":

    if len(args) >= 1:
        with urllib.request.urlopen(args[1]) as response:
            print(response.getheader('X-Request-Id'))
