#!/usr/bin/python3

for i in "zyxwvutsrqponmlkjihgfedcba":
    to_uppercase = 0
    if ord(i) % 2 != 0:
        to_uppercase = 32
    else:
        to_uppercase = 0

    print("{}".format(chr(ord(i) - to_uppercase)), end='')
