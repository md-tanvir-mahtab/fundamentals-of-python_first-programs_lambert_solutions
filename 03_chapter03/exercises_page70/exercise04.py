"""
Program: exercise04.py
Author: Md. Tanvir Mahtab
Date: 2022-01-15

Problem:
    Write a loop that prints the first 128 ASCII values followed by the corresponding
    characters (see the section on characters in Chapter 2). Be aware that most of the
    ASCII values in the range “0..31” belong to special control characters with no stan-
    dard print representation, so you might see strange symbols in the output for these
    values.

Solution:
    >>>
"""


# Loop for printing the first 128 ASCII values along with corresponding characters
for value in range(128):
    print("ASCII value: {} and corresponding character: {}".format(value, chr(value)))
