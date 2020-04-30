#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    if x % 2 != 0:
        print("{}".format(chr(x - (33 - 1))), end='')
# FIRST PRINT FOR LOWER !=
    else:
        print("{}".format(chr(x)), end='')
# SECOND PRINT IS FOR UPPER
