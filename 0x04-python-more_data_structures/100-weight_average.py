#!/usr/bin/python3


def weight_average(my_list=[]):
    numerator = 0
    denominator = 0
    evarage = numerator / denominator

    for elements in my_list:
        numerator += (elements[0] * elements[1])
        denominator += elements[1]

    return evarage
