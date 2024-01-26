#!/usr/bin/python3
"""
    takes in a URL,
    sends a request to the URL and displays the body of the response.
"""


if __name__ == '__main__':
    import sys
    import requests

    with requests.get(sys.argv[1]) as res:
        if res.status_code >= 400:
            print('Error code: {}'.format(res.status_code))
        else:
            print(res.text)
