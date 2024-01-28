#!/usr/bin/python3
"""
1-top_ten.py

This module provides a function to fetch the top ten posts in a
given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """Fetch the top ten posts in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")

    for c in results.get("children"):
        print(c.get("data").get("title"))
