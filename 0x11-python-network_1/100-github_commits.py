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
                  'https://api.github.com/repos/{}/{}/commits?per_page=10'
                  .format(sys.argv[2], sys.argv[1]),
                  headers=headers
                ) as res:
        for commit in res.json():
            print('{}: {}'.format(
                commit.get('sha'),
                  commit.get('commit')
                        .get('author')
                        .get('name')))
