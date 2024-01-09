#!/usr/bin/python3
def uppercase(str):
    to_uppercase = 0
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            to_uppercase = 32
        else:
            to_uppercase = 0
        print("{}".format(chr(ord(i) - to_uppercase)), end='')
    print()
