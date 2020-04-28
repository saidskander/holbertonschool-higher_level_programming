#!/usr/bin/python3
x = 0
for i in range(97, 123):
  if i == ord("q") or i == ord("e"):
   continue
  print(chr(i), end="")
# other example: print("{:c}".format(i), end="")
