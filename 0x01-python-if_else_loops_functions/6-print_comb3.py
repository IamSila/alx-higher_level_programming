#!/usr/bin/python3
for a in range(0, 10, 1):
    for b in range(a+1, 10, 1):
        if (a == 8) and (b == 9):
            print("{}{}".format(a, b))
        else:    
            print("{}{}, ".format(a, b), end='')
