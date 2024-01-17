#!/usr/bin/python3

"""
0-subs.py

This module provides a function to fetch the number of subscribers for a
given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit: str) -> int:
    """Fetch the number of subscribers for a given subreddit"""

    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    
    res = requests.get(url, headers={'User-Agent': 'aeflheim/0.0.1',
                                     'Content-Type': 'application/json'},
                       params={'limit': 10},
                       allow_redirects=False)

    if res.status_code == 302:
        return 0

    data: dict = res.json().get('data')
    return int(data.get('subscribers')) if data.get('subscribers') else 0
