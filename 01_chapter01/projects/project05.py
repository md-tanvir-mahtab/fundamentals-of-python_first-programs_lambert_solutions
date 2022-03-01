"""
Author: Md. Tanvir Mahtab
Date: 2021-11-26
Program: project05.py
Problem:
    Modify the program of Project 4 to compute the area of a triangle. Issue the
    appropriate prompts for the triangle’s base and height, and change the names of
    the variables appropriately. Then, use the formula .5 * base * height to com-
    pute the area. Test the program from an IDLE window.
Solution:
    >>>
"""

# Take input
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))

# Calculate the area
area = 0.5 * base * height

# Display the result
print("The are of the triangle is", area)
