#!/usr/bin/python3
"""importing requests module and sys packag"""
import requests
import sys
def get_request_id(url):
    try:
        res = requests.get(url)
        x_request_id = res.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("Request id not found")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e)
        exit()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        exit()
    url = sys.argv[1]
    get_request_id(url)
