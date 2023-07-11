#!/usr/bin/python3
"""Module that inherits from
BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
