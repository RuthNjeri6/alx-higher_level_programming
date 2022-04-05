#!/usr/bin/python3
""" Module that prints new lines"""


def text_indentation(text):
    """ Function that prints new lines after `.`, `:` or ´?´"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    else:
        checks = '?.:'
        new_text = text.strip()
        for i, char in enumerate(new_text):
            if char in checks:
                print(char, end="")
                print('\n')
            else:
                if char == ' ' and (new_text[i - 1] in checks):
                    pass
                else:
                    print(char, end="")
