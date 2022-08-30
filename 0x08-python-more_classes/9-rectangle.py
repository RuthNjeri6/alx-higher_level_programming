#!/usr/bin/python3
"""Module that defines a class"""


class Rectangle:
    """defines class rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __int__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError('width must be an integer')
        if not value >= 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError('height must be an integer')
        if not value >= 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = []
        if self.__width == 0 or self.height == 0:
            return ''
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return ''.join(rect)

    def __repl__(self):
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rectangle based on area"""
        if not isinstance(Rectangle, rect_1):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(Rectangle, rect_2):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1 > rect_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        cls.__width = cls.__height = size
        return cls()
