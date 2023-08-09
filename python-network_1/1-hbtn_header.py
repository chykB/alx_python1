#!/usr/bin/python3
"""importing requests module and sys packag"""
import requests
import sys
def get_x_request_id(url):
  """Gets the value of the X-Request-Id header in the response to a request to the specified URL."""
  response = requests.get(url)
  return response.headers['X-Request-Id']
if __name__== "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    print(x_request_id)
