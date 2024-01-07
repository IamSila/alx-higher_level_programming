#!/usr/bin/python3
import sys
arg_length = len(sys.argv[1:])
if arg_length == 1:
    print(f"{arg_length} argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(f"{arg_length} arguments: ")
    for i in range(1,arg_length):
        print(f"{i}: {sys.argv[i]}")
