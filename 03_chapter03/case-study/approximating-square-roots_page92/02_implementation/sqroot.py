"""
Program: sqroot.py
Author (Motivated by the book's author): Md. Tanvir Mahtab
Date: 2022-02-08

Purpose: This script contains a function that can compute the square root of a given
number using Newton's approximation method.
"""

# Define the function to compute square root
def compute_square_root(input_number):
    """
    Takes a floating-point positive number, computes the square root of it using 
    Newton's approximation method, and returns the result.
    """

    # Initialize variables
    input_number = input_number
    tolerance = 0.000001
    estimate = 1.0

    # Approximate the square root
    while True:
        estimate = (estimate + input_number / estimate) / 2
        difference = abs(input_number - estimate ** 2)
        if difference <= tolerance:
            break
    
    # Return the estimate
    return estimate