#!/usr/bin/python3
"""script that takes in 3 strings and sends a search request to
the Twitter API"""
import requests
import base64
import sys


if __name__ == "__main__":
    key = sys.argv[1]
    secret = sys.argv[2]

    encoded = base64.b64encode(bytes("{}:{}".format(key, secret)
                                     .encode('utf-8')))
    header = {"Authorization": "Basic " + str(encoded, encoding='utf-8'),
              "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    req = requests.post("https://api.twitter.com/oauth2/token",
                        headers=header, data={"grant_type":
                                              "client_credentials"})
    token = req.json().get("access_token")
    headers_aut = {"Authorization": "Bearer " + token}
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {'q': sys.argv[3], 'count': 5}
    req2 = requests.get(url, params=params, headers=headers_aut)
    for r in req2.json().get("statuses"):
        print("[{}] {} by {}".format(
            r.get('id'), r.get('text'), r.get('user').get('name')))
