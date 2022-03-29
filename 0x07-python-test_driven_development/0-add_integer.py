#!/usr/bin/python3
""" Add numbers """


def add_integer(a, b=98):
    """Function that adds 2 numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    try:
        a = int(a)
        if not float('-inf') < float(a) < float('inf'):
            raise TypeError('a must be an integer')
    except Exception as err:
        raise TypeError('a must be an integer')
    try:
        b = int(b)
        if not float('-inf') < float(a) < float('inf'):
            raise TypeError('a must be an integer')
    except Exception as err:
        raise TypeError('b must be an integer')
    return (a + b)
