"""
Program: pi.py
Author: Md. Tanvir Mahtab
Date: 2022-02-14

Purpose: This script contains a function that can approximate the value of pi using 
Leibniz's approximation method.
"""

# Define the function
def approximate_pi(iterations):
    """
    Takes the number of iterations as argument, computes the approximated value of pi 
    using Leibniz's method, and returns it.
    """
    # Initialize a variable to
    # hold the approximated sum
    sum = 0.0

    # Initialize a variable to
    # hold the sign of arithmetic operation
    sign = "+"

    # Approximate pi
    for iteration in range(1, iterations+1):
        if sign == "+":
            sum += 1 / (2 * iteration - 1)
            sign = "-"
        else:
            sum -= 1 / (2 * iteration - 1)
            sign = "+"
    
    # Return sum by multiplying 4 with it
    # to complete the formula
    return 4 * sum