#!/usr/bin/python3
"""Funct which writes a string to a text file"""


def write_file(filename="", text=""):
    """This funct which writes a string
    to a text file and give the number of characters
    written"""

    n_characters = 0

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

    n_characters = len(text)

    return n_characters
