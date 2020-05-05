#!/usr/bin/python3
def no_c(my_string):
    empty = ""
    for x in my_string:
        if x not in 'cC':
            empty += x
    return empty
