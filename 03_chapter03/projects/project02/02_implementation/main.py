"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-11

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import triangle

# Define the main function
def main():
    # Take the lengths of the sides of the triangle
    # as inpts (The inputs should be floating-point numbers)
    side_a = float(input("Enter the length of one side of the tirangle: "))
    side_b = float(input("Enter the length of another side: "))
    side_c = float(input("Enter the length of the remaining side: "))

    # Call the function to check
    # if the triangle is a right triangle
    triangle_status = triangle.is_right_triangle(side_a, side_b, side_c)

    # Display if the triangle is a right triangle
    if triangle_status:
        print("The triangle is a right triangle.")
    else:
        print("The triangle is not a right triangle.")

# Execution point of the program
if __name__ == "__main__":
    main()