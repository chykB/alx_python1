#!/usr/bin/python3
"""import request and sys"""
import requests
import sys
def main():
  url = sys.argv[1]
  res = requests.get(url)

  print(res.text)
  if res.status_code >= 400:
    print("Error code: {} ".format(res.status_code))

if __name__ == "__main__":
  main()
