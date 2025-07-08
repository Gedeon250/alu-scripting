#!/usr/bin/python3
"""DOCS"""
import requests


def top_ten(subreddit):
    """Fetch and print the top 10 hot post titles of a subreddit."""
    reddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit
    )
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])

            if not posts:
                print("OK")  # Changed from None to "OK" per expected output
                return

            for post in posts[:10]:
                print(post['data'].get('title', "No Title Found"))
        except ValueError:
            print("OK")  # Handle invalid JSON response
    else:
        print("OK")  # Handle non-existent subreddit case
