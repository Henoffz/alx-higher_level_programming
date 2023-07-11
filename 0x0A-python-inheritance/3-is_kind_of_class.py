#!/usr/bin/python3
"""
This module contains a function that returns
True if the obj is exactly an instance of the
specified class else False
"""


def is_kind_of_class(obj, a_class):
    """function that returns true if obj is
    an instance of an inherited class.
    """
    return isinstance(obj, a_class)
