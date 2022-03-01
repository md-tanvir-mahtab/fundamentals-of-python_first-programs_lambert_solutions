"""
Program: number_guessing.py
Author: Md. Tanvir Mahtab
Date: 2022-02-12

Purpose: This script contains a function that can let the computer guess a number
from within the given range of lower and upper bounds and check if it is correct.
"""

# Import required module(s)
import math

# Define the function
def guess_number(lower_bound, upper_bound):
    """
    Takes lower and upper bounds of a range as inputs, lets the computer guess a 
    number from within the range upto a spceific number of times, checks the guess 
    based on the user's hint and diplays if the guess is correct or not.
    """

    # Get the ideal number of maximum attempts
    max_attempts = math.ceil(math.log2(upper_bound - lower_bound + 1))

    # Initialize the counter
    count = 0
    
    # Initialize the flag
    flag = 0

    # Perform guessing and check it
    while count < max_attempts:
        # Update the counter
        count += 1

        # Compute the guessing number
        # Here the division should be an integer division
        guess = (lower_bound + upper_bound) // 2

        # Display the guess
        print("The number is", guess)

        # Take feedback or hints from the user
        hint = input("Enter = or < or > accordingly: ")

        # Proceed according to the hint
        if hint == "=":
            print("Guessed correctly in {} attempt(s).".format(count))
            flag = 1
            break
        elif hint == "<":
            upper_bound = guess - 1
        elif hint == ">":
            lower_bound = guess + 1
    
    # Display this message
    # if the computer fails to guess correctly
    # within the specified maximum number of attempts
    if flag != 1:
        print("Failed to guess correctly within the maximum number of attempts, and you might cheated.")