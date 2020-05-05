#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    dup = my_list[:]
    if idx >= 0:
        return dup[idx] = element
    if idx < len(dup):
        return dup[idx] = element
    return dup
