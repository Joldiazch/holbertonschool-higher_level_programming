#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
from urllib import request, parse
from sys import argv as args

if __name__ == "__main__":

    if len(args) >= 2:
        URL, email = args[1], args[2]
        values = {
            'email': email
        }
        data = parse.urlencode(values).encode('ascii')
        with request.urlopen(URL, data) as response:
            htmt = response.read()
            print(htmt.decode('utf-8'))
