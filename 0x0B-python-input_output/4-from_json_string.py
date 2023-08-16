#!/usr/bin/python3
"""file that returns the JSON representation of an string"""
import json


def from_json_string(my_str):
    """function hat return JSON rep of an string"""
    return json.loads(my_str)
