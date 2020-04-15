#!/usr/bin/python3
"""
Script that takes 2 arguments in order to list 10 commits (from the most recent
to oldest) of the repository received as first argument by the user received as
second argument
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    req = requests.get(url).json()
    if req:
        for count, res in enumerate(req):
            if count < 10:
                if isinstance(res, dict):
                    print("{}: {}".format(res.get("sha"),
                          res.get("commit").get("author").get("name")))
            else:
                break
