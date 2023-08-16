#!/usr/bin/python3
""""creates a class student with
public atrtributes"""


class Student:
    """defines attributes for the class"""
    def __init__(self, first_name, last_name, age):
        """instantiation of the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary rep of class"""
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})
