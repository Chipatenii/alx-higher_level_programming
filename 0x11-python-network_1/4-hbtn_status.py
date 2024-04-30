#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests


def fetch_alx_intranet_status():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    fetch_alx_intranet_status()
