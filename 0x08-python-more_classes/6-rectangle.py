#!/usr/bin/python3
"""Module for a class rectangle"""


class Rectangle():
    """defines class rectangle"""
    number_of_instances = 0

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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        return self.__height

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns a string representation of object"""
        if self.__width == 0 or self.__height == 0:
            return ''
        rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                rec.append('#')
            if i != self.__height - 1:
                rec.append('\n')
        return (''.join(rec))

    def __repr__(self):
        """returns a string representation of instance"""
        return "Rectangle(" + str(self.__width) + ", " \
            + str(self.__height) + ")"

    def __del__(self):
        """deletes instance"""
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
