#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == "__main__"):
    argc = len(argv)
    result = 0
    operators = ["+", "-", "*", "/"]

    if (argc != 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    if (argv[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    number1 = int(argv[1])
    operator = argv[2]
    number2 = int(argv[3])

    if (operator == "+"):
        result = add(number1, number2)
    elif (operator == "-"):
        result = sub(number1, number2)
    elif (operator == "*"):
        result = mul(number1, number2)
    else:
        result = div(number1, number2)
    print("{:d} {:s} {:d} = {:d}".format(number1, operator, number2, result))
    