#!/usr/bin/python3
"""DOCS"""
import requests

def top_ten(subreddit):
    """Fetch and print the top 10 hot post titles of a subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            if not posts:
                print("OK", end="")
                return
            for post in posts[:10]:
                print(post['data'].get('title', "No Title Found"))
        except ValueError:
            print("OK", end="")
    else:
        print("OK", end="")
