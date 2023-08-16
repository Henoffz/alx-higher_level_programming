#!/usr/bin/python3
"""
Module that contains
inherits from a list
"""


class MyList(list):
    """A child class that inherits
    from a parent class.
    """
    def print_sorted(self):
        print(sorted(self))
