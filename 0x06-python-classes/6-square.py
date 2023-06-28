#!/usr/bin/python3
""" Definition of Square class."""


class Square:
    """Initializes square, determines size, calculates area, prints"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes instance of square

        Args:
            size: Size of square
            position: Position to indent square
        """
        self.size = size
        self.position = position

    def area(self):
        """Determines area"""
        return self.size ** 2

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Gets position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position

        Args:
            value: Value of position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not all(isinstance(num, int) for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif any(num < 0 for num in value):
            raise ValueError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """Prints square offsetting it by position with symbol #"""
        if self.size == 0:
            print('')
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
