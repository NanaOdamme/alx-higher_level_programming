#!/usr/bin/python3
"""
Uses Basic Authentication with a personal access token
to access GitHub API and display user id.
Usage: ./10-my_github.py <username> <token>
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, token)
    response = requests.get(url, auth=auth)
    print(response.json().get('id', None))
