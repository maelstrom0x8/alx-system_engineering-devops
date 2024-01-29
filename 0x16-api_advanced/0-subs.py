#!/usr/bin/python3
"""
0-subs.py

This module provides a function to fetch the number of subscribers for a
given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """Fetch the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    try:
        results = response.json().get("data")
        return results.get("subscribers")
    except Exception:
         return 0
