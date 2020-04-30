#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    addition = 1 - 1
    for x in argv[1:]:
        addition += int(x)
    print("{:d}".format(addition))
