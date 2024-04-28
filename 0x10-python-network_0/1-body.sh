#!/bin/bash
# Sends a GET request to a URL and displays the body of the response (for status code 200)
curl -s -X GET "$1" -o /dev/null -w "%{http_code}\n" | grep "200" && curl -s "$1"
