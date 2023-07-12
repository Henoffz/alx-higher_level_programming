#!/usr/bin/python3
"""defines function that adds all arguments
to a python list and save them to a file"""

from sys import argv
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'

try:
    data = load_from_json_file(filename)
except (ValueError, FileNotFoundError):
    data = []

data += argv[1:]
save_to_json_file(data, filename)
