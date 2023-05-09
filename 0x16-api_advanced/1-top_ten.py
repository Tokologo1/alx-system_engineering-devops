#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit"""
import request

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "httpd://www.reddit.com/r/{}/hot/.json".format
    (subreddit)
    headers = {
            "User-Agent": "Linux:0x16.advanced:v1.0.0 (by /u/bdov_)"
    }
    param = {
        "limit": 10
    }
    response = request.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
