#!/usr/bin/python3
"""
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import sys
    import requests
    import json

    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    with requests.get(
                  'https://api.github.com/repos/{}/{}/commits'
                  .format(sys.argv[1], sys.argv[2]),
                  headers=headers
                ) as res:
        for commit in res.json():
            print(commit.get('sha') + ':', commit.get('author').get('login'))
