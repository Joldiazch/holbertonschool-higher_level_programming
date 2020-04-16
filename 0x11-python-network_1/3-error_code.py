#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
from urllib import request, parse
from sys import argv as args
from urllib.error import URLError

if __name__ == "__main__":

    URL = args[1]
    try:
        with request.urlopen(URL) as response:
            htmt = response.read()
        print(htmt.decode('utf-8'))
    except URLError as e:
        print('Error code: {}'.format(e.code))
