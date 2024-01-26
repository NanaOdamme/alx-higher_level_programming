#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of X-Request-Id from the header.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')

        if x_request_id:
            print(x_request_id)
        else:
            print("Header 'X-Request-Id' not found in the response.")
