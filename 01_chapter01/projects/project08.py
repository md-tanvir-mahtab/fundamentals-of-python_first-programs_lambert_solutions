"""
Author: Md. Tanvir Mahtab
Date: 2021-11-26
Program: project08.py
Problem:
    Enter an input statement using the input function at the shell prompt. When the
    prompt asks you for input, enter a number. Then, attempt to add 1 to that num-
    ber, observe the results, and explain what happened.
Solution:
    >>>
"""

# Take input
var1 = input("Enter the input: ")

# Perform calculation (will show TypeError; since a number can't be added to a string)
var2 = var1 + 1

# Display the result
print(var2)