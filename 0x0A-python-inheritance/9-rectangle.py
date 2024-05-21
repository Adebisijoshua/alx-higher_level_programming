#!/usr/bin/python3
"""inherit at BaseGeometry"""


class BaseGeometry:
    """It is a public instance method"""

    def area(self):
        """calculate  the area"""
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        """checks value"""
        x = type(value)
        if x is not int:
            raise TypeError("{} has to be an integer".format(name))
        if value <= 0:
            raise ValueError("{} has to be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle inherit on BaseGeometry"""

    def __init__(self, width, height):
        """initialization of privates"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """implementing area"""
        return self.__width * self.__height

    def __str__(self):
        """give a str representation"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
