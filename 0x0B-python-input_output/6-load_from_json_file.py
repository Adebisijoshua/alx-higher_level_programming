#!/usr/bin/python3
""" Make object from a JSON file """
import json


def load_from_json_file(filename):
    """ Function which creates an Object from a “JSON file” """
    with open(filename, 'r') as f:
        return (json.load(f))
