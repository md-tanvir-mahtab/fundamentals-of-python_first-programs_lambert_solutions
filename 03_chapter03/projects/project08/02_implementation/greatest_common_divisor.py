"""
Program: greatest_common_divisor.py
Author: Md. Tanvir Mahtab
Date: 2022-02-26

Purpose: This script contains a function that can compute the greatest common divisor
of two positive integers using Euclidean algorithm.
"""

# Define the function
def gcd(larger, smaller):
    """
    Takes two positive integers as inputs, compute the Greatest Common Divisor (GCD)
    of those using Euclidean algorithm, and displays the GCD along with the status of
    each step of the algorithm.
    """

    # Keep copies of the given numbers
    given_larger = larger
    given_smaller = smaller

    # Declare a variable
    # to track the step number
    step = 0

    # Execute the Euclidean algorithm
    while smaller != 0:
        # Specify the current step
        step += 1

        # Display the current step number
        print("-------- Step", step, "----------")

        # Display the initial values
        # of larger and smaller numbers
        # of the current step
        print("Initial larger number:", larger)
        print("Initial smaller number:", smaller)

        # Compute the remainder of dividing
        # the larger number by the smaller number
        remainder = larger % smaller

        # Display the remainder
        print("Remainder:", remainder)

        # Update the larger and smaller numbers
        larger = smaller
        smaller = remainder

        # Display the final values
        # of larger and smaller numbers
        # of the current step
        print("Final larger number:", larger)
        print("Final smaller number:", smaller)
    
    # Display the GCD
    print("The GCD of {} and {} is {}.".format(given_larger, given_smaller, larger))