#!/usr/bin/python3
"""Read the lines of the File"""


def read_lines(filename="", numberoflines=0):
    """reading lines"""
    with open(filename, 'r', encoding='utf8') as File:
        n = sum(1 for line in open(filename))
        if numberoflines <= 0 or numberoflines > n:
            print(File.read(), end="")
        else:
            for line in range(0, numberoflines):
                print(File.readline(), end="")
    File.closed
