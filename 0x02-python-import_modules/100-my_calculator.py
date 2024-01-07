#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    a = int(sys.argv[1])
    b = (int(sys.argv[3]))
    operator = sys.argv[-2]
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }
    argument_len = len(sys.argv)
    if (argument_len - 1) != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    elif (sys.argv[2]) not in operations.keys():
        print("Unknown operator. Available operators: +, -, * and /")

    print("{}{}{} = {}".format(a, operator, b, operations[sys.argv[2]](a, b)))
