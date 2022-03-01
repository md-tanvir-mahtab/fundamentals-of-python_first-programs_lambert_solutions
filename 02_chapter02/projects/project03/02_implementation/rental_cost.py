"""
Program: rental_cost.py
Author: Md. Tanvir Mahtab
Date: 2022-01-02

Purpose: This script contains a function for calculating total rental cost of videos.
"""

# Define the functiion for calculating total rental cost
def calculate_total_cost(num_new_video, num_oldie_video):
    # Define the rental costs of each type of videos as constant
    NEW_VIDEO_COST = 3.00
    OLDIE_VIDEO_COST = 2.00
    
    # Calculate total rental cost
    total_cost = NEW_VIDEO_COST * num_new_video + OLDIE_VIDEO_COST * num_oldie_video

    # Return total rental cost
    return total_cost