#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    last = number % -10
    print('Last digit of', number, 'is')
if last > 5:
    print(last, "and is greater than 5", end=' ')
elif last == 0:
    print(last, "and is 0", end=' ')
else:
    print(last, "and is less than 6 and not 0", end=' ')
