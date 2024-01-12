#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length == "\0":
        length = None
        return length, first
    else:
        return length, first
