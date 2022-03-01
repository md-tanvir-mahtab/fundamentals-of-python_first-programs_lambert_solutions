"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-09

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import triangle

# Define the main function
def main():
    # Take the lengths of the sides of the triangle as inputs
    # Inputs should be floating-point numbers
    side_a = float(input("Enter the length of a side of the triangle: "))
    side_b = float(input("Enter the length of another side: "))
    side_c = float(input("Enter the length of the remaining side: "))

    # Call the function to check
    # if the triangle is equilateral
    result = triangle.is_equilateral(side_a, side_b, side_c)

    # Display if the triangle is equilateral
    if result:
        print("The triangle is equilateral.")
    else:
        print("The triangle is not equilateral.")

# Execution point of the program
if __name__ == "__main__":
    main()