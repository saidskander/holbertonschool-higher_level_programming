#!/usr/bin/python3
"""Python script that takes in a URL,
   sends a request to the URL and displays the body of the response
   (decoded in utf-8"""

import urllib.request
import urllib.error
from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error Code: {}".format(error.code))
