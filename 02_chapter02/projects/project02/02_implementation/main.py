"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-02

Purpose: This is the main script of the project.
"""

# Import required module(s)
import cube_surface_area

# Define the main function
def main():
    # Input the length of an edge of the cube as an integer
    edge_length = int(input("Enter the length of an edge of the cube: "))

    # Call the function for calculating the surface area of the cube
    surface_area = cube_surface_area.calculate_area(edge_length)

    # Print the surface area
    print("The surface area of the cube is", surface_area, "cubic unit.")

# Execution point of the program
if __name__ == "__main__":
    main()