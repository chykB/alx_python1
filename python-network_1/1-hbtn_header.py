#!/usr/bin/python3
"""importing requests module and sys packages"""

import requests
"""requests module"""
import sys
"""sys package"""

def get_x_request_id(url):
    """Gets the value of the X-Request-Id header in the response to a request to the specified URL"""
    response = requests.get('https://alu-intranet.hbtn.io/status')
    return response.header['X-Request-Id']


if__name__=='__main__':
    """execute the script when it is run as a standalone program."""
    url = sys.argv[1]
    print(get_x_request_id(url))
