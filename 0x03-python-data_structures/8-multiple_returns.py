#!/usr/bin/python3


def multiple_returns(sentence):
    """returns two value the length and the first character"""
    if len(sentence) == 0:
        sentence[0] = None
    return len(sentence), sentence[0]
