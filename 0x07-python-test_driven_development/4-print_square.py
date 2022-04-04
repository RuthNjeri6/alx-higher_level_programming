#!/usr/bin/python3
""" Module to print a square """


def print_square(size):
    """ Function that prints a square """
    if type(size) is int and size >= 0:
        for i in range(0, size):
            for j in range(0, size):
                print('#', end='')
            print('')
    elif type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    elif type(size) is int and size < 0:
        raise ValueError('size must be >= 0')
    else:
        raise TypeError('size must be an integer')
