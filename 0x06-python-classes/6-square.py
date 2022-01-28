#!/usr/bin/python3
"""CLass Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        if (type(position) is tuple and len(position) == 2
                and position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')
            return
        [print('') for x in range(0, self.__position[1])]
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(' ', end='')
            for j in range(0, self.__size):
                print('#', end='')
            print('')
