#!/usr/bin/python3
"""Sends a GET request to the specified URL and prints the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

def main():
  """Sends a GET request to the specified URL and prints the body of the response."""
  url = sys.argv[1]

  res = requests.get(url)

  if res.status_code >= 400:
    print('Error code: {}'.format(res.status_code))
    sys.exit(1)
  else:
    print(res.text)

if __name__ == '__main__':
  main()
