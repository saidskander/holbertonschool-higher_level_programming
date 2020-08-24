#!/usr/bin/python3
"""Python script that takes in a URL and an email"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    inp = {'email': argv[2]}
    data = urllib.parse.urlencode(inp)
    data2 = data.encode("ascii")
    req = urllib.request.Request(argv[1], data2)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
