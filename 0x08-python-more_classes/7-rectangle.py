#!/usr/bin/python3
"""Module that defines a class rectangle"""


class Rectangle():
    """defines class rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0 ")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an interger")
        elif value < 0:
            raise ValueError("height must be >= 0 ")
        else:
            self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ''
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return (''.join(rect))

    def __repr__(self):
        return "Rectangle (" + str(self.__width) + ', ' \
            + str(self.__height) + ')'

    def __del__(self):
        if Rectangle.number_of_instances > 0:
            print('Bye rectangle...')
            Rectangle.number_of_instances -= 1
