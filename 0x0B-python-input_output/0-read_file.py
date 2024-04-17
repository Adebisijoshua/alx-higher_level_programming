#!/usr/bin/python3
"""This will defines a text file-reading function"""


def read_file(filename=""):
    """gives the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
