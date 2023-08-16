#!/usr/bin/python3
"""defines a function that returns the dictionary
description with simple data structure"""


def class_to_json(obj):
    """returns dictionary description"""
    return (obj.__dict__)
