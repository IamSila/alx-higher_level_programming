#!/usr/bin/python3


weight_evarage = __import__("100-weight_evarage").weight_evarage

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]

result = weight_evarage(my_list)
print("Average: {:0.2f}".format(result))
