#!/usr/bin/python3


def weight_evarage(my_list=[]):
    """calculates the weighted evarage of values in a tuple"""
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for element in my_list:
        numerator += element[0] * element[1]
        denominator += element[1]
    weightedAverage = numerator / denominator
    return weightedAverage
