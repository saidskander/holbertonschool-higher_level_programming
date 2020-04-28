#!/usr/bin/python3
for number1 in range(0, 8):
    for number2 in range(number1 + 1, 10):
        print("{:d}{:d}".format(number1, number2), end=', ')
print("{:d}{:d}".format(number1 + 1, number2))
