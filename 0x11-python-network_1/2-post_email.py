#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request to the passed URL
    with the email as parameter, and displays the body of the response
"""


if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    req = urllib.request.Request(

            url,
            f"email={email}".encode('ascii'),
            method='POST'
        )

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
