"""
Author: Md. Tanvir Mahtab
Date: 2021-11-26
Program: project07.py
Problem:
    Write and test a program that accepts the user’s name (as text) and age (as a number)
    as input. The program should output a sentence containing the user’s name and age.
Solution:
    >>>
"""

# Take input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Display name and age
print("Your name is", name, "and age is", age)
# Dispalay name and age (alternative)
print("Your name is {} and age is {}".format(name, age))
# Display name and age (another alternative)
print(f"Your name is {name} and age is {age}")