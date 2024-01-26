#!/usr/bin/python3
"""
Sends a request to a given URL and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the HTTP status code in case of an error.
Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body_content = response.read().decode('utf-8')
            print(body_content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
