#!/usr/bin/python3
"""
Module that inherits from a parent class.
"""


class BaseGeometry:
    """class with two public instances"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle with private instances.
    """
    def __init__(self, width, height):
        """
        initializing instances.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        prints string
        """
        return('[Rectangle] {:d}/{:d}'.format(self.__width, self.__height))


class Square(Rectangle):
    """
    Square that inherits from rectangle
    """
    def __init__(self, size):
        """
        initializing class attributes.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        returns area of square
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        prints string.
        """
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
