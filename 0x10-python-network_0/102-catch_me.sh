#!/bin/bash
# Sends a request to a URL that causes the server to respond with a specific message
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me -H "Referer: HolbertonSchool"
