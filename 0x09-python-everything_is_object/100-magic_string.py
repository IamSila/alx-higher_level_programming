#!/usr/bin/python3
def magic_string(checker={"counter": 0}):
    checker["counter"] += 1
    return (', '.join(['BestSchool'] * (checker['counter'])))
