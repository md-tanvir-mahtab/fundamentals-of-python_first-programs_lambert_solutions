"""
Program: exercise04.py
Author: Md. Tanvir Mahtab
Date: 2022-01-27

Problem:
    Write a loop that outputs the numbers in a list named salaries . The outputs should 
    be formatted in a column that is right-justified, with a field width of 12 and a 
    precision of 2.

Solution:
    >>>
"""

# Initialize the vairable
salaries = [213.46, 3121.79, 15342.17]

# Display the elements of the list
for salary in salaries:
    print("%12.2f" % salary)