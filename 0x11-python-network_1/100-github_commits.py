#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
of a repository by a user using the GitHub API.
Usage: ./100-github_commits.py <repository_name> <owner_name>
"""
import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repository_name)

    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            a_name = commit.get('commit', {}).get('author', {}).get('name')
            print(f"{sha}: {a_name}")
    else:
        print(f"Error: HTTP Status Code:{response.status_code}")
