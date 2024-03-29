#!/usr/bin/python3
"""
Sends a request to a given URL and displays the
value of X-Request-Id from the header.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    """Retrieve the value of X-Request-Id from the response header"""
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)
