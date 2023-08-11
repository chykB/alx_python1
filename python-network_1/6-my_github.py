#!/usr/bin/python3
"""this program uses the GitHub API to display my id"""
import requests
import sys

def github_d(username, password):
    url = 'https://api.github.com/users/{}'.format(username, password)
    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.json()['id']
    else:
        print("Error: {}".format(response.status_code))
        sys.exit(1)

if __name__ == "__main__":
    username =  sys.argv[1]
    password = sys.argv[2]
    id = github_d(username, password)
    print("{}".format(id))
