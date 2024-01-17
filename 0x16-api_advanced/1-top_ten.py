#!/usr/bin/python3

"""
1-top_ten.py

This module provides a function to fetch the top ten posts in a
given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """Fetch the top ten posts in a subreddit"""
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'aeflheim/0.0.1',
                                     'Content-Type': 'application/json'},
                       params={'limit': 10}, allow_redirects=False)

    sc = res.status_code
    if sc in [302, 404]:
        print('None')
        return

    data = res.json().get('data')
    i = 1
    for item in data.get('children'):
        if i > 10:
            break
        print(item.get('data').get('title'))
        i += 1
