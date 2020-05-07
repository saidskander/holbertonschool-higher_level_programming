#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = a_dictionary.copy()
    for i, x in dictionary.items():
        dictionary[i] = x * 2
    return dictionary
