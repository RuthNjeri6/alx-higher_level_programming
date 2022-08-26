#!/usr/bin/python3
"""Module that defines a class"""


class Rectangle():

    """Defines a class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=1):
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
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __del__(self):
        if Rectangle.number_of_instances > 0:
            print('Bye rectangle...')
            Rectangle.number_of_instances -= 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rect = []
        for i in range(0, len(self.__height)):
            for j in range(0, len(self.__width)):
                rect.append(Rectangle.print_symbol)
            if i != len(self.__height) - 1:
                rect.append('\n')
        return (''.join(rect))

    def __repl__(self):
        return 'Rectangle (' + str(self.__width) + ', ' + \
            str(self.__height) + ')'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            bigger_rect = rect_2
        elif rect_1.area() > rect_2.area():
            bigger_rect = rect_1
        else:
            bigger_rect = rect_1
        return bigger_rect
