#!/usr/bin/python3
"""file that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function hat return JSON rep of an obj"""
    return json.dumps(my_obj)
