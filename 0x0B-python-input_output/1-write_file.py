#!/usr/bin/python3
"""
file that contains functiom
that writes a string to a text file
and returns number of character written.
"""


def write_file(filename="", text=""):
    """function that returns number of lines written"""
    with open(filename, mode="w", encoding="utf-8") as file:
        abc = file.write(text)
        return abc
