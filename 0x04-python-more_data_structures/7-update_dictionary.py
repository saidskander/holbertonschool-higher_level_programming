#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    x = 0
    for valueKey in a_dictionary:
        if valueKey == key:
            a_dictionary[valueKey] = value
            x = 1
    if x == 0:
        a_dictionary[key] = x
    return a_dictionary
