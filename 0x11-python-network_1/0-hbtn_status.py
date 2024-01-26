#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib.
Displays information about the response body.
"""
import urllib.request

def fetch_and_display_status(url):
    """function to fetch and displau status"""

    with urllib.request.urlopen(url) as response:
        body_content = response.read()

        print("Body response:")
        print(f"\t- type: {type(body_content)}")
        print(f"\t- content: {body_content}")
        print(f"\t- utf8 content: {body_content.decode('utf-8')}")


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_and_display_status(url)
