"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-12

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import distance

# Define the main function
def main():
    # Take initial height (a floating-point number) in feet and
    # number of times (an integer) of bouncing as inputs
    initial_height = float(input("Enter the initial height (in Feet): "))
    times = int(input("Enter the number of times of bouncing: "))

    # Call the function to calculate the total distance
    total_distance = distance.calculate_distance(initial_height, times)

    # Display the total distance
    print("Total distance traveled is {} feet.".format(total_distance))

# Execution point of the program
if __name__ == "__main__":
    main()