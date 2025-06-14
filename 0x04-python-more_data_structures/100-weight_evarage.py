#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for elements in my_list:
        numerator += elements[0] * elements[1]
        denominator += elements[1]

    evarage = numerator / denominator
    return evarage
