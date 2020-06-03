#!/usr/bin/python3
"""Reading text Func"""


def read_file(filename=""):
    """reading a file"""
    with open(filename, "r", encoding="utf8") as File:
        Result = File.read()
    print("{}".format(Result), end="")
