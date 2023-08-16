#!/usr/bin/python3
"""creates a class
student with defined attributes"""


class Student:
    """defines attributes for the class"""

    def __init__(self, first_name, last_name, age):
        """instantiation of the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary rep of class"""
        return (self.__dict__)
