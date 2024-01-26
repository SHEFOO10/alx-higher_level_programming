#!/usr/bin/python3
"""
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import sys
    import requests

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer {}'.format(sys.argv[2]),
        'X-GitHub-Api-Version': '2022-11-28'
    }
    with requests.get('https://api.github.com/user', headers=headers) as res:
        print(res.json().get('id'))
