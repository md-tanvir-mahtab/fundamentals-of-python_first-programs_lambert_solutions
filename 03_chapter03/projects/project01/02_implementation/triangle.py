"""
Program: triangle.py
Author: Md. Tanvir Mahtab
Date: 2022-02-09

Purpose: This script contains a function that can check if a triangle is equilateral
based on the length of its three sides.
"""

# Define the function
def is_equilateral(side_a, side_b, side_c):
    """
    Takes the length of the three sides of a triangle and returns a boolean indicating
    whether the triangle is equilateral or not.
    """
    # Return True if all the sides are equal
    # otherwise return False
    if side_a == side_b and side_b == side_c:
        return True
    else:
        return False