#!/usr/bin/python3
import math


class MagicClass:
    """ class that create circumference of a circle"""
    def __init__(self, radius=0):
        """initializing class objects."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """defining area."""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """defining circumference."""
        return ((2 * math.pi) * self.__radius)
