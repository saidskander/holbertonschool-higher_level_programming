#!/usr/bin/python3
"""func numbers of lines"""


def number_of_lines(filename=""):
    """number of lines in the File"""
    numberoflines = 0
    with open(filename, 'r', encoding='utf8') as File:
        for x in File:
            numberoflines = numberoflines + 1
    File.closed
    return (numberoflines)
