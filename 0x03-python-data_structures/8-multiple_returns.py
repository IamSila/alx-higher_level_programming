#!/usr/bin/python3


def multiple_returns(sentence):
    """returns two value the length and the first character"""

    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return length, first
