#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id
    in the response header
"""


if __name__ == '__main__':
    import sys
    import requests

    with requests.get(sys.argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
