#!/usr/bin/python3
"""Module that defines a class"""


class Rectangle():
    """Class defining a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes objects of class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width"""
        return self.__width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
        return self.__height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns # character representing the dimensions of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ('')
        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append('\n')
        return (''.join(rec))

    def __repr__(self):
        """returns a string representation of instance"""
        return "Rectangle(" + str(self.__width) + ", " \
            + str(self.__height) + ")"
