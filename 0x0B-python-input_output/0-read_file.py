#!/usr/bin/python3
"""
File that contains a function that
prints text file to stdout.
"""


def read_file(filename=""):
    """reads a text file and prints it
    in stdout.
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
