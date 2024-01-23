#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        a / b
    except Exception:
        return None
    return a / b
