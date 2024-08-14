#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.

Requirements:

Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""

import requests


def top_ten(subreddit):
    """
    The function described above
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    headers = {'User-Agent': 'MyBot/0.1'}  # Custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                print(title)
        else:
            print("None")
    else:
        print("None")
