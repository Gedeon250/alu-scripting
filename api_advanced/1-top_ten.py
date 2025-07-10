#!/usr/bin/python3
"""Fetch top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post["data"].get("title"))
    else:
        print(None)
