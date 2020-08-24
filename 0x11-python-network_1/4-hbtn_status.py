#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

from requests import get

fetch = get("https://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(fetch.text)))
print("\t- content: {}".format(fetch.content.decode('utf-8')))
