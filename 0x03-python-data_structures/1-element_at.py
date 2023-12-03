#!/usr/bin/python3
#  File Name 1-element_at.py
# Adekunle Joshua Adebisi  Adekunle8k@gmail.com


def element_at(my_list, idx):
    """Retrive an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
