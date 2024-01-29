#!/usr/bin/python3

"""
2-recurse.py

This script defines a function 'recurse' that retrieves a list of the titles
of the hottest posts from a given subreddit on Reddit.
"""
import requests


import requests

def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves titles of the hottest posts from a given
    subreddit on Reddit.
    """
    if hot_list is None:
        hot_list = []

    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        results = requests.get(url, params=params, headers=user_agent, allow_redirects=False)
        results.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    data = results.json().get("data")
    after_data = data.get("after")

    if after_data:
        recurse(subreddit, hot_list, after=after_data)

    all_titles = data.get("children")
    hot_list.extend(title_.get("data").get("title") for title_ in all_titles)

    return hot_list

if __name__ == '__main__':
    # Example usage
    subreddit_titles = recurse('python')
    print(subreddit_titles)

