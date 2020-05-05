#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxint = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > maxint:
            maxint = my_list[x]
    return maxint
