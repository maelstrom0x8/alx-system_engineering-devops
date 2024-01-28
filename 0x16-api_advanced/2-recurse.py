#!/usr/bin/python3

"""
2-recurse.py

This script defines a function 'recurse' that retrieves a list of the titles
of the hottest posts from a given subreddit on Reddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursively retrieves titles of the hottest posts from a given
    subreddit on Reddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"after": after, "count": count, "limit": 100}
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    res = requests.get(url, params=params, headers=headers,
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
