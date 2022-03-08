"""
Program: exercise03.py
Author: Md. Tanvir Mahtab
Date: 2022-03-08

Problem:
    Assume that the variable myString refers to a string. Write a code segment that
    uses a loop to print the characters of the string in reverse order.

Solution:
    >>>
"""

# Take input for the variable myString
myString = input("Enter a string: ")

# Print the characters of the string
# in reverse order
for index in range(1, len(myString) + 1):
    print(myString[-index], end = " ")

print("")

# Alternative approach
for index in range(len(myString)-1, -1, -1):
    print(myString[index], end = " ")

print("")