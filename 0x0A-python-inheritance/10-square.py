#!/usr/bin/python3
"""Gets a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """present a square"""

    def __init__(self, size):
        """set a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
