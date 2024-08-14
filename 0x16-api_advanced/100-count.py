#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java shouldn't
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    The function as require above
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
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_c = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_c:
                    print(f"{word}: {count}")
