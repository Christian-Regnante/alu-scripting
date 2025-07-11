#!/usr/bin/python3
"""
Recursively retrieves all hot article titles for a given subreddit using the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot articles
    for the given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): Used to accumulate article titles recursively.
        after (str): The pagination token from Reddit API.

    Returns:
        list: List of article titles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Python:recurse:v1.0 (by /u/yourusername)'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if subreddit is invalid
        if response.status_code != 200:
            return None

        data = response.json().get('data')
        if not data:
            return None

        children = data.get('children')
        for child in children:
            hot_list.append(child['data']['title'])

        # Recursive call with next page token
        if data.get('after') is not None:
            return recurse(subreddit, hot_list, data.get('after'))

        return hot_list

    except Exception:
        return None

