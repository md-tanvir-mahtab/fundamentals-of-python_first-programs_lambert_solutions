"""
Program: exercise02.py
Author: Md. Tanvir Mahtab
Date: 2022-03-08

Problem:
    Assume that the variable data refers to the string "myprogram.exe" . Write the
    expressions that perform the following tasks:
    a. Extract the substring "gram" from data.
    b. Truncate the extension ".exe" from data.
    c. Extract the character at the middle position from data.

Solution:
    >>>
"""

# Import required module(s)
import math

# Initialize the variable
data = "myprogram.exe"

# Code for (a)
print(data[5:9])

# Code for (b)
print(data[:9])

# Alternative apporach for (b)
print(data[:-4])

# Code for (c)
print(data[math.ceil(len(data)/2) - 1])