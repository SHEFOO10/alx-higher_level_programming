#!/usr/bin/python3
"""
    takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    import sys
    with requests.post(

            'http://0.0.0.0:5000/search_user',
            {'q': sys.argv[1] if len(sys.argv) > 1 else ''}
         ) as res:
        try:
            content = res.json()
            if (len(content) == 0):
                print('No result')
            else:
                print('[{}] {}'.format(content.get('id'), content.get('name')))
        except Exception:
            print('Not a valid JSON')
