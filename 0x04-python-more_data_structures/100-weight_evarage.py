#!/usr/bin/python3


def weight_evarage(my_list=[]):
    """calculates the weighted evarage of values in a tuple"""

    result = 0
    total = 0

    if not my_list:
        return 0

    for i in my_list:
        result += i[0] * i[1]
        total += i[1]
    weightedAverage = result / total
    return weightedAverage
