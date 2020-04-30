#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv) - 1
    print("{} {:s}{:s}".format(l,
                                 "argument" if l <= 2 else "arguments", "." if l == 1 else ":"))
    for x, n in enumerate(argv):
        if x > 0:
            print("{:d}: {:s}".format(x, n))
