#!/usr/bin/python3
"""
A  function that queries the Reddit API and returns the number of subscribers.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.
    If no results are found or subreddit is invalid, returns None.
    """
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALU-Reddit-API/0.1'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get('data', {})
        children = data.get('children', [])
        if not children and not hot_list:
            return None
        for post in children:
            hot_list.append(post['data'].get('title'))
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None

