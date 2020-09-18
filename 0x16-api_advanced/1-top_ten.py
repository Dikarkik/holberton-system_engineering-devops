#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
If not a valid subreddit, print None.

NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.

python3 1-main.py programming
python3 1-main.py this_is_a_fake_subreddit
"""

import json
import requests


def top_ten(subreddit):
    headers = {'user-agent': 'fake_user_agent'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        posts = json.loads(request.text)['data']['children']
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print('None')


if __name__ == "__main__":
    top_ten('programming')
