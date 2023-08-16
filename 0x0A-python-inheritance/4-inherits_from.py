#!/usr/bin/python3
"""module:_____"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to be compared against.

    Returns:
        bool: True if the object is an instance of a class that inherited
              from the specified class, otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
