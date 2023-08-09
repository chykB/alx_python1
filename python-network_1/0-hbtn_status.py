#!/usr/bin/python3
"""this module is use to make a request"""
import requests
if __name__=="__main__":
    response = requests.get('http://0.0.0.0:5050/status')
    if response.status_code == 200:
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    else:
        print(response.status_code)
