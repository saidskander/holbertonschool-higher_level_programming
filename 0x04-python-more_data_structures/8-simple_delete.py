#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    x = 0
    for rmKey in a_dictionary:
        if rmKey == key:
            x = 1
    if x == 1:
        del a_dictionary[key]
    return a_dictionary
