#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ordkey in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(ordkey, a_dictionary[ordkey]))
