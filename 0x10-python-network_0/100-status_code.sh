#!/bin/bash
#sends a request to a URL passed as an argument, and displays status code
curl -sw "%{http_code}" $1 -o /dev/null
