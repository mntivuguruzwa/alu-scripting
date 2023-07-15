#!/usr/bin/python3
"""docs"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None
    else:
        json_res = response.json()
        after = json_res['data'].get('after')
        has_next = after is not None
        hot_articles = json_res['data'].get('children')
        [hot_list.append(article['data'].get('title')) for article in hot_articles]

        return recurse(subreddit, hot_list, after=after) 
            if has_next else hot_list
