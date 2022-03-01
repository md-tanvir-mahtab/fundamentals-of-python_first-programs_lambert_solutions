"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-02

Purpose: This is the main script of the project.
"""

# Import required module(s)
import sphere

# Define the main function
def main():
    # Take the radius of the sphere as input
    radius = float(input("Enter the radius of the sphere: "))

    # Call the function for calculating the requested attribures of the sphere
    diameter, circumference, surface_area, volume = sphere.calculate_attributes(radius)

    # Print the attributes
    print("Different attributes of the sphere are:")
    print("Diameter:", diameter, "unit")
    print("Circumference:", circumference, "unit")
    print("Surface area:", surface_area, "square unit")
    print("Volume:", volume, "cubic unit")

# Execution point of the program
if __name__ == "__main__":
    main()