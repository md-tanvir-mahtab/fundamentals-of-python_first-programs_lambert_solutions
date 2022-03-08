"""
Program: exercise04.py
Author: Md. Tanvir Mahtab
Date: 2022-03-08

Problem:
    Assume that the variable myString refers to a string, and the variable
    reversedString refers to an empty string. Write a loop that adds the characters
    from myString to reversedString in reverse order.

Solution:
    >>>
"""

# Take input for the variable myString
myString = input("Enter a string: ")

# Initialize the variable reversedString
reversedString = ""

# Add the characters from myString
# to reversedString in reverse order
for index in range(1, len(myString)+1):
    reversedString += myString[-index]

# Display reversedString
print(reversedString)