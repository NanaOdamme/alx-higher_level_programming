#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a repository by a user using the GitHub API.
Usage: ./100-github_commits.py <repository_name> <owner_name>
"""
import sys
import requests

if __name__ == "__main__":
    # GitHub repository and user information
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API endpoint for repository commits
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    # Parameters for the GitHub API request
    params = {'per_page': 10}  # Retrieve 10 commits

    # Make the GET request to the GitHub API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract and display commit information
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name')
            print(f"{sha}: {author_name}")
    else:
        # Display an error message if the request was not successful
        print(f"Error: Unable to fetch commits. HTTP Status Code: {response.status_code}")
#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a repository by a user using the GitHub API.
Usage: ./100-github_commits.py <repository_name> <owner_name>
"""
import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name')
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commits. HTTP Status Code: {response.status_code}")

