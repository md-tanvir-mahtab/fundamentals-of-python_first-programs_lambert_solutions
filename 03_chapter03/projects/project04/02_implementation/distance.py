"""
Program: distance.py
Author: Md. Tanvir Mahtab
Date: 2022-02-12

Purpose: This script contains a function that can calculate total distance traveled by
a ball based on its initial height and number of times of bouncing.
"""

# Define the function
def calculate_distance(initial_height, times):
    """
    Takes initial height and number of times of bouncing as inputs, computes total 
    distance traveled, and returns it.
    """
    # Initialize the total distance
    total_distance = 0.0

    # Compute the distance
    for time in range(1, times+1):
        distance = initial_height + initial_height * 0.6

        # Update the total distance
        total_distance += distance

        # Update the initial height
        initial_height *= 0.6
    
    # Return the total distance
    return total_distance