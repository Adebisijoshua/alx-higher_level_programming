#!/usr/bin/python3
"""This module defines ll a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text afte each of the line containing a given string in a file
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
