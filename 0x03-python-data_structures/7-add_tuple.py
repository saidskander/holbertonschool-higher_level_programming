#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = ()
    for x in (tuple_a, tuple_b):
        if len(x) == 0:
            x = (0, 0)
        elif len(x) == 1:
            x = (x[0], 0)
        if i == ():
            i = x
    return x[0] + i[0], x[1] + i[1]
