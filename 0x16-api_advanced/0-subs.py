#!/usr/bin/python3
"""Function to query subcribbers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the toal number on a given Reddit subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Linux:0x16.api.advance:v10.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
