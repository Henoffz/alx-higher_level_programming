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

    @property
    def size(self):
        """retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """setting the new value of square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with the # character."""
        for i in range(self.__size):
            print("#" * self.__size, end='')
            print('')
        if self.__size == 0:
            print('')
