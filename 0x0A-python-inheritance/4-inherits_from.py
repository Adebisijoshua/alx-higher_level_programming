#!/usr/bin/python3
"""
The inherits_from function
"""


def inherits_from(obj, a_class):
    """gives yes if obj is a subclass of a_class, or else No"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)i
