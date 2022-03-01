"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-14

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import pi

# Define the main function
def main():
    # Take input
    iterations = int(input("Enter the number of iterations: "))

    # Call the function to approximate pi
    approximated_pi = pi.approximate_pi(iterations)

    # Display the result
    print("The approximated value of pi after {} iteration(s) is {}".format(iterations,
        approximated_pi))

# Execution point of the program
if __name__ == "__main__":
    main()