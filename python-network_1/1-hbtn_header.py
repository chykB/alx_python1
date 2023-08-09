#!/usr/bin/python3
"""importing requests module and sys packag"""
import requests
import sys
def get_x_request_id(url, x_request_id):
  """Gets the value of the X-Request-Id header in the response to a request to the specified URL."""
  headers = {'X-Request-Id':x_request_id}
  response = requests.get(url, headers=headers)
  return response.headers['X-Request-Id']
if __name__== "__main__":
    if len(sys.argv) <==1:
        sys.exit(1)
    url = sys.argv[1]
    x_request_id = sys.argv[2]
    result = get_x_request_id(url, x_request_id)
    print(result)
