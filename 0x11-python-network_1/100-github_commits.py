#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest) of a specified repository by a specified user.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
