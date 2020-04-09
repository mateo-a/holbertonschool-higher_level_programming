#!/bin/bash
#sends a JSON POST request to a URL passed as argument, and displays the body
curl -sH "Content-Type: application/json" -d @$2 $1
