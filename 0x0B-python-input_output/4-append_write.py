#!/usr/bin/python3
"""append write in text file"""


def append_write(filename="", apptext=""):
    """using append"""
    with open(filename, 'a', encoding='utf8') as File:
        x = str(apptext)
        return(File.write(x))
