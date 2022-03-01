"""
Program: exercise03.py
Author: Md. Tanvir Mahtab
Date: 2022-02-03

Problem:
    Write a loop that counts the number of space characters in a string. Recall that 
    the space character is represented as ' '.

Solution:
    >>>
"""

# Take a string as input
sample_string = input("Enter the string: ")

# Initialize a counter variable
counter = 0

# Count the number of space characters
for index in range(len(sample_string)):
    if sample_string[index] == " ":
        counter += 1

# Display the number of space characters
print("There are {} space character(s) in {}".format(counter, sample_string))