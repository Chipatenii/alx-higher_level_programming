#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using the urllib package.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html_content = response.read()
        decoded_content = html_content.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(html_content))
        print("\t- content:", html_content)
        print("\t- utf8 content:", decoded_content)
