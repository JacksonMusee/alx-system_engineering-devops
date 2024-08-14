#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

Prototype: def recurse(subreddit, hot_list=[])
You may change the prototype, but it must be able to be called with just a
subreddit supplied.
AKA you can add a counter, but it must work without supplying
a starting value in the main.

If not a valid subreddit, return None.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.

Your code will NOT pass if you are using a loop and not recursively
calling the function!
This /can/ be done with a loop but the point is to use a recursive function.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    The function as required above
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'MyBot/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                hot_list.append(title)
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
