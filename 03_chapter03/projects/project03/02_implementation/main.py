"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-12

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import number_guessing

# Define the main function
def main():
    # Take lower and upper bounds as inputs
    # The inputs should be integers
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    # Call the function to guess the number
    number_guessing.guess_number(lower_bound, upper_bound)

# Execution point of the program
if __name__ == "__main__":
    main()