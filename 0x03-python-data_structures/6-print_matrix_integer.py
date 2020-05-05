#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    em = ''
    for x in matrix:
        em += "\n"
        for g in x:
            em += "{:d} ".format(g)
        em = em[:-1]
    print("{}".format(em[1:]))
