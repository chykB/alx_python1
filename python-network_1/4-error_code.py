#!/usr/bin/python3
"""Sends a GET request to the specified URL and prints the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

def get_response(url):
  """Sends a GET request to the specified URL and prints the body of the response."""
  res = requests.get(url)
  return res

if __name__ == "__main__":
  url = sys.argv[1]
  res = get_response(url)
  print("HTTP status code:", res.status_code)
  
  if res.status_code > 400:
    print('Error code: {}'.format(res.status_code))
  else:
    print(res.text)
