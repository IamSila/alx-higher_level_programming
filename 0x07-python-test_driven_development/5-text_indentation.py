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
      - text: str
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    delimitors = '.:?'
    final_text = text

    for delimitor in delimitors:
        final = f'{delimitor}\n\n'.join(
            (list(map(lambda w: w.strip(' '), final_text.split(delimitor))))
        )
    print(final_text, end='')
