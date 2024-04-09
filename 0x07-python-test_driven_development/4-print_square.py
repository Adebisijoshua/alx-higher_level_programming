#!/usr/bin/python3
"""Define the function that gives a square with the character #.

Attributes of the square:
    print_square: function that prints a square with the character #.
"""      


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size of the square (1 side).

    Raises any issues:
        TypeError: If size is not an integer and less than 0.
        ValueError: If size is less than 0.
    """
    message = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(message)

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
