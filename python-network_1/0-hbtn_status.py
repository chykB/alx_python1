#!/usr/bin/python3
"""this module is use to make a request"""
import requests
if __name__=="__main__":
    response = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
