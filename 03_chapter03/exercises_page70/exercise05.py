"""
Program: exercise05.py
Author: Md. Tanvir Mahtab
Date: 2022-01-15

Problem:
    Assume that the variable teststring refers to a string. Write a loop that prints
    each character in this string, followed by its ASCII value.

Solution:
    >>>
"""


# Assign an arbitrary string to the variable teststring
teststring = "sample_string"

# Loop for printing each character of the string along with its ASCII value
for character in teststring:
    print("Character: {} and corresponding ASCII value: {}".format(character, ord(character)))
