#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter """
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        req = requests.post(url, data={"q": ""})
    else:
        req = requests.post(url, data={"q": sys.argv[1]})
    try:
        jason = req.json()
        if not jason:
            print("No result")
        else:
            print("[{}] {}".format(jason.get("id"), jason.get("name")))
    except ValueError:
        print("Not a valid JSON")
