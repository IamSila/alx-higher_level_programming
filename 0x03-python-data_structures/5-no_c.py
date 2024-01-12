#!/usr/bin/python3

def no_c(my_string):
    if my_string != "\n": 
        for x in range(0, len(my_string), 1):
            if my_string[x] == 'c' or my_string[x] == 'C':
                return my_string[:x] + my_string[x+1:]
