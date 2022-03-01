"""
Program: main.py
Author (Motivated by the book's author: Md. Tanvir Mahtab
Date: 2022-02-08

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import sqroot
import math

# Define the main function
def main():
    # Take input (as a floating-point number) from the user
    input_number = float(input("Enter a positive number to get its square root: "))

    # Call the function to compute the square root
    square_root = sqroot.compute_square_root(input_number)

    # Display the result
    print("The square root (evaluated by the program) of {} is {}".format(input_number,
        square_root))
    
    # Display the result evaluated by the
    # math.sqrt function for comparison
    print("The square root (evaluated by math.sqrt()) of {} is {}".format(input_number,
        square_root))

# Execution point of the program
if __name__ == "__main__":
    main()