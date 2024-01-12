#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    two_factors = []
    for element in my_list:
        if element % 2 == 0:
            two_factors.append(True)
        else:
            two_factors.append(False)
    return two_factors
