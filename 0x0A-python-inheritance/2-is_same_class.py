#!/usr/bin/python3
"""Module that contain is_same_class method"""


def is_same_class(obj, a_class):
    """Returns:
    True: if the object is exactly the  instance of the specified class
    False: otherwise"""
    return type(obj) == a_class
