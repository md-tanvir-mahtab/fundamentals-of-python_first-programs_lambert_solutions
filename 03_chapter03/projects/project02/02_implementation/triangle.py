"""
Program: triangle.py
Author: Md. Tanvir Mahtab
Date: 2022-02-11

Purpose: This script contains a function that can check if a triangle is a right
triangle using Pythagorean theorem.
"""

# Define the function
def is_right_triangle(side_a, side_b, side_c):
    """
    Takes the lengths of the three sides of a triangle as inputs, checks if it is
    a right triangle based on the Pythagorean theorem, and returns True/False 
    accordingly.
    """
    # Specify the hypotenuse (longest side)
    if side_a > side_b:
        if side_a > side_c:
            hypotenuse = side_a
        else:
            hypotenuse =side_c
    else:
        if side_b > side_c:
            hypotenuse = side_b
        else:
            hypotenuse = side_c
    
    # Seperate the lengths of the adjacent sides
    # from the possible hypotenuse (i.e. take a list/collection
    # of the lengths of the sides excluding the one which
    # equals to the possibe hypotenuse)
    sides_list = [side_a, side_b, side_c]
    sides_list.remove(hypotenuse)
    adjacent_sides = sides_list

    # Check if the Pythagorean formula holds true
    # for the given inputs and return Boolean type
    # True or False based on it
    if hypotenuse ** 2 == adjacent_sides[0] ** 2 + adjacent_sides[1] ** 2:
        return True
    else:
        return False