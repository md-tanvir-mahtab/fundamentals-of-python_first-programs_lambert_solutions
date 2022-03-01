"""
Program: exercise02.py
Author: Md. Tanvir Mahtab
Date: 2022-02-03

Problem:
    Assume that x refers to a number. Write a code segment that prints the number's 
    absolute value without using Python's abs function.

Solution:
    >>>
"""

# Take input for x
x = float(input("Enter the number: "))

# Get the absolute value of the number
if x < 0:
    x = -x

# Display the absolute value
print("The absolute value is", x)