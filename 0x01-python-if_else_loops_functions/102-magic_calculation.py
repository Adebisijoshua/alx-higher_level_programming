#!/usr/bin/python3
# File name : 102-magic_calculation.py
# Adekunle Joshua Adebisi Adekunle8k@gmail.com


def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)i
