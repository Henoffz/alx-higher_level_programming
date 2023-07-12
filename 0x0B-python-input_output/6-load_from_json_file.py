#!/usr/bin/python3
"""defines a function that creates an Object from a “JSON file”."""
import json


def load_from_json_file(filename):
    """creates an object from json file."""
    with open(filename) as my_file:
        return (json.load(my_file))
