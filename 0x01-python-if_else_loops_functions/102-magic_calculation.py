#!/usr/bin/python3
# File name : 102-magic_calculation.py
# Adekunle Joshua Adebisi Adekunle8k@gmail.com

def magic_calculation(a, b, c):
    if a < b:
        return (c)
    elif c > b:
        return (a + b)
    else:
        return (a * b - c)
