"""
Program: exercise04_alt_solution.py
Author: Md. Tanvir Mahtab
Date: 2022-02-03

Problem:
    Assume that the variables x and y refer to strings. Write a code segment that prints
    these strings in alphabetical order. You should assume that they are not equal.

Solution:
    >>>
"""

# Take inputs
x = input("Enter a string: ")
y = input("Enter another string (Different from the first one): ")

# Check the equality of the strings
# and prompt for the correct inputs if required
while x == y:
    print("Input strings must be different.")
    
    # Take correct inputs
    x = input("Enter a string: ")
    y = input("Enter another string (Different from the first one): ")

# Arrange the strings in alphabetical order
if x < y:
    first_string = x
    second_string = y
else:
    first_string = y
    second_string = x

# Display the strings in alphabetical order
print(first_string, second_string)