#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
Displays information about the response body.
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
