#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")# print positive number
elif number == 0:
    print(f"{number} is zero")# print zero number
elif number < 0:
    print(f"{number} is negative")# print negative number
