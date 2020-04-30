#!/usr/bin/python3
from sys import argv


def main():
    print('{} argument'.format(len(argv) - 1), end='')
    if len(argv) <= 2:
        print('s.')
    elif len(argv) >= 2:
        print(':')
    else:
        print('s:')
    for x in range(1, len(argv)):
        print('{}: {}'.format(x, argv[x]))

if __name__ == "__main__":
    main()
