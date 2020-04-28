#!/usr/bin/python3
for letter_asc in range(ord('a'), ord('z')+1):
    x = chr(letter_asc)
    if x not in "qe":
    print(x, end='')
