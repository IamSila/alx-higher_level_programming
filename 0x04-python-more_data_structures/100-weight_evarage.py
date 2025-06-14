#!/usr/bin/python3


def weight_evarage(my_list=[]):
    """calculates the weighted evarage of values in a tuple"""
    result = 0
    total = 0
    if len(my_list) == 0:
        return 0
    for i in range(len(my_list)):
        result += my_list[i][0] * my_list[i][1]
        total += my_list[i][1]
    weightedEvarage = result / total
    return weightedEvarage
