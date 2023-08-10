#!/usr/bin/python3
"""requests module and sys package"""
import requests
import sys
def post_email(url, email):
    """Sends a POST request to the specified URL with the specified email address as a parameter"""
    response = requests.post(url, data={"email":email})
    return response.text
if __name__== "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    url = 'http://localhost:5000/receive_email'
    email = sys.argv[1]
    response = post_email(url, email)
    print(response)
