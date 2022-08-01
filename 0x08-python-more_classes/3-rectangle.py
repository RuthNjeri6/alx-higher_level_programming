#!/usr/bin/python3
"""Module that defines a class"""


class Rectangle():
    """Class Rectangle"""
    def __init__(self, width=0, height=0):
        """initializes instances from class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
            return self.__width

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
        return self.__height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns # representation of object"""
        if self.__width == 0 or self.__height == 0:
            return ''
        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append('\n')
        return (''.join(rec))
