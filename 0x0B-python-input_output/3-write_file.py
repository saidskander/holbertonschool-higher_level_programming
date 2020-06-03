#!/usr/bin/python3
"""Func to write a file"""


def write_file(filename="", FileText=""):
    """wr File"""
    with open(filename, 'w') as File:
        result = File.write(FileText)
    File.closed
    return result
