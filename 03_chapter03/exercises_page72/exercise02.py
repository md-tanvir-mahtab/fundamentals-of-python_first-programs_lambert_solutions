"""
Program: exercise02.py
Author: Md. Tanvir Mahtab
Date: 2022-01-27

Problem:
    Write a code segment that displays the values of the integers x , y , and z on a 
    single line, such that each value is right-justified with a field width of 6.

Solution:
    >>>
"""

# Initialize the variables
x, y, z = 9, 99, 999

# Display the values of the variables
for value in [x, y, z]:
    print("%6d" % value)