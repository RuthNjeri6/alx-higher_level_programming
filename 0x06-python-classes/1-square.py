#!/usr/bin/python3
"""Create a square class with a private instance attribute"""


class Square:
    """Class with private instance attribute size"""
    def __init__(self, size):
        self.__size = size
