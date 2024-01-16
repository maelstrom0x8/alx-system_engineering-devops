#!/usr/bin/python3

"""
0-subs.py

This module provides a function to fetch the number of subscribers for a
given subreddit using the Reddit API.
"""

import requests


def fetch_subscribers(subreddit: str):
    """Fetch the number of subscribers for a given subreddit"""
    url = f"https://api.reddit.com/r/{subreddit}/about"
    res = requests.get(url, headers={'User-Agent': 'Agent-Smith V1'})
    content = res.json()
    data: dict = content.get('data')
    return int(data.get('subscribers')) if data.get('subscribers') else 0
