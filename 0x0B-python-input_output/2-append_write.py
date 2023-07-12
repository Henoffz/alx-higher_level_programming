#!/usr/bin/python3
"""
file that contains function that appends
a string at the end of a text file and
returns number of characters added
"""


def append_write(filename="", text=""):
    """function that append a sring at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
