#!/usr/bin/python3
"""
This module contains a function that returns
True if the obj is exactly an instance of the
specified class else False
"""


def is_same_class(obj, a_class):
    """check if object is an instance of class"""
    if type(obj) == a_class:
        return True
    return False
