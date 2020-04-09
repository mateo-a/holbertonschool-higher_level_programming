#!/bin/bash
#takes URL as argument, sends a GET request to the URL, and displays the body
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" $1
