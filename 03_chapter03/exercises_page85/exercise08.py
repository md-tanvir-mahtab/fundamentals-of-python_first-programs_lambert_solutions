"""
Program: exercise08.py
Author: Md. Tanvir Mahtab
Date: 2022-02-03

Problem:
    The variables x and y refer to numbers. Write a code segment that prompts the user 
    for an arithmetic operator and prints the value obtained by applying that operator 
    to x and y.

Solution:
    >>>
"""

# Take inputs
x = float(input("Enter a number (Left operand): "))
y = float(input("Enter another number (right operand): "))
operator = input("Enter an arithmetic operator (+, -, *, /): ")

# Perform the arithmetic operation
# and display the result
if operator == "+":
    print("The result is", x + y)
elif operator == "-":
    print("The result is", x - y)
elif operator == "*":
    print("The result is", x * y)
elif operator == "/":
    while y == 0:
        print("The divisor (right operand) can't be zero")
        # Take a valid input for y
        y = float(input("Enter another number (right operand): "))
    else:
        print("The result is", x/y)