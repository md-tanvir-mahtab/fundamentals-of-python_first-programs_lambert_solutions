"""
Author: Md. Tanvir Mahtab
Date: 2021-11-26
Program: project06.py
Problem:
    Write and test a program that computes the area of a circle. This program should
    request a number representing a radius as input from the user. It should use the formula
    3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
Solution
    >>>
"""

# Take input
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = 3.14 * radius ** 2

# Display the result
print("The area of the circle is", area)