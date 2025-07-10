#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.

If the subreddit is invalid, it prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Python:api_advanced:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
    except requests.RequestException:
        print("None")
        return

    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print("None")
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
