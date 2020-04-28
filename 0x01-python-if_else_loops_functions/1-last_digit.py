#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
    print('Last digit of', number, 'is', end=' ')
else:
    last = number % 10
    print('Last digit of', number, 'is', end=' ')
if last > 5:
    print(last, 'and is greater than 5')
elif last == 0:
    print(last, 'and is 0')
else:
    print(last, 'and is less than 6 and not 0')
