#!/usr/bin/python3
"""
This module prevent a user from
dynamically creating new instance attribute.
Except- new instance attribute = first_name.
"""


class LockedClass:
    """
    A class with no class or object attribute
    """

    __slots__ = "first_name"

    def __init__(self):
        """Attempt to create new instance
        based on the existing condition"""

        self.first_name = "first_name"
