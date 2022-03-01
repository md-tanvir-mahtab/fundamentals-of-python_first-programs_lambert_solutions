"""
Program: exercise02.py
Author: Md. Tanvir Mahtab
Date: 2022-02-07

Problem:
    The factorial of an integer N is the product of the integers between 1 and N, inclu-
    sive. Write a while loop that computes the factorial of a given integer N.

Solution:
    >>>
"""

# Take input
while True:
    number = int(input("Enter a non-negative integer to get its factorial: "))
    # Check if the number is non-negative
    if number == abs(number):
        break

# Initialize the counter
count = 1

# Initialize the product
product = 1

# Compute the factorial
while count <= number:
    if number==0 or number==1:
        break
    else:
        product = product * count
        count += 1

# Display the factorial
print("The factorial of {} is {}".format(number, product))