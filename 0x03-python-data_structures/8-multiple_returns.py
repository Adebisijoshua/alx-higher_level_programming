#!/usr/bin/python3
# File Name : 8-multiple_returns.py
# Author : Adekunle Joshua Adebisi  <375@holbertonschool.com>


def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
