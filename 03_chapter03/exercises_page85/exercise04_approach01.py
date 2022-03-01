"""
Program: exercise04.py
Author: Md. Tanvir Mahtab
Date: 2022-02-03

Problem:
    Assume that the variables x and y refer to strings. Write a code segment that prints
    these strings in alphabetical order. You should assume that they are not equal.

Solution:
    >>>
"""

# Take inputs
x = input("Enter a string: ")
y = input("Enter another string (Different from the first one): ")

# Check the equality of inputs and
# prompt for the correct inputs if required
while x == y:
    print("Input strings must be different.")
    
    # Take inputs
    x = input("Enter a string: ")
    y = input("Enter another string (Different from the first one): ")


# Arrange the strings in alphabetical order
if len(x) == len(y):
    for index in range(len(x)):
        if x[index] < y[index]:
            first_string = x
            second_string = y
            break
        elif x[index] > y[index]:
            first_string = y
            second_string = x
            break
else:
    flag = 0
    for index in range(len(min(x, y))):
        if x[index] < y[index]:
            first_string = x
            second_string = y
            flag = 1
            break
        elif x[index] > y[index]:
            first_string = y
            second_string = x
            flag = 1
            break
    
    if flag != 1:
        first_string = min(x, y)
        second_string = max(x, y)

# Display the strings in alphabetical order
print(first_string, second_string)