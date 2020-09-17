#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of
subscribers for a given subreddit. If an invalid subreddit is given,
the function should return 0.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.

python3 0-main.py programming
python3 0-main.py this_is_a_fake_subreddit
"""

import json
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Diana'}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    request = requests.get(url, headers=headers, allow_redirects=False)
    if request.status_code == 200:
        data = json.loads(request.text)
        return data['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    number_of_subscribers('programming')
