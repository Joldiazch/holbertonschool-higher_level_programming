#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        msg = [
            'Body response:',
            '   - type: {}'.format(type(html)),
            '   - content: {}'.format(html),
            '   - utf8 content: {}'.format(html.decode("utf-8"))
        ]
        for line in msg:
            print(line)
