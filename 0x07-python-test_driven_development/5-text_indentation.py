#!/usr/bin/python3

"""
This program takes a text and search the delimitors (?, : and .)
if find this characters insert two new lines after this delimitors
an print the result.
"""


def text_indentation(text):
    """
    text_indentation: Insert two new lines after the delimitors ?, : and .
    After that print the result.
     Args:
        text: holds the string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimitors = '.:?'
    formated_text = text

    for delimitor in delimitors:
        formated_text = f"{delimitor}\n\n".join(
        (list(map(lambda word: word.strip(' '), formated_text.split(delimitor))))
        )
    print(formated_text, end='')
