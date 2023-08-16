#!/usr/bin/python3
""" Definition of Square class."""


class Square:
    """A class with private attributes."""

    def __init__(self, size=0):
        """Initializes private attributes of class.

        Args:
            size: square size.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the instance Square."""
        result = self.__size ** 2
        return result
