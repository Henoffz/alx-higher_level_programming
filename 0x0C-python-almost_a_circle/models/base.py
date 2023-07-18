#!/usr/bin/python3
"""Defines a base class for other classes
in this project"""

import json
import os
import csv


class Base:
    """
    Class with private class attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return serialized list of a dictionary"""
        if list_dictionaries is None or not list_dictionaries:
            return []
        return (json.dump(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation of a list object to a file"""
        filename = cls.__name__ + '.json'
        my_list = []
        if list_objs is not None:
            for obj in list_objs:
                my_list.append(cls.to_dictionary(obj))
        with open(filename, "w+") as my_file:
            my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """return deserialized list of json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + '.json'
        try:
            if os.path.exists(file_name):
                with open(file_name, "r") as my_file:
                    my_list = cls.from_json_string(my_file.read())
                    for i in range(len(my_list)):
                        my_list[i] = cls.create(**my_list[i])
                        return my_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save object list in CSV file"""
        file_name = cls.__name__ + '.csv'
        with open(file_name, "w+") as csvfile:
            if list_objs is None or not list_objs:
                csvfile.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    names = ["id", "width", "height", "x", "y"]
                else:
                    names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=names)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads object list from a CSV file"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, newline="") as my_file:
                reader = csv.DictReader(my_file)
                my_list = []
                for dictionary in reader:
                    for key, value in dictionary.items():
                        dictionary[key] = int(value)
                    my_list.append(dictionary)
            return [cls.create(**dictionary) for dictionary in my_list]
        except FileNotFoundError:
            return []
