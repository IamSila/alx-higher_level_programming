#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_number.keys())

    number = 0
    last_rom = 0
    list_number = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if roman_number.get(ch) <= last_rom:
                    num += to_subtract(list_number)
                    list_number = [roman_number.get(ch)]
                else:
                    list_number.append(roman_number.get(ch))

                last_rom = roman_number.get(ch)

    num += to_subtract(list_number)

    return (num)