#!/usr/bin/python3
"""
Module that contains a class
with public instance.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square that inherits from rectangle
    """
    def __init__(self, size):
        """
        initializes a square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
