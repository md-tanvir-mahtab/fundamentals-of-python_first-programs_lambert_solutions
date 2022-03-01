"""
Program: sphere.py
Author: Md. Tanvir Mahtab
Date: 2022-01-02

Purpose: This script contains a function that calculates different attributes of 
a sphere based on its given radius.
"""

# Define the function for calculating different attributes of a sphere
def calculate_attributes(radius):
    """
    Returns the diameter, circumference, surface area and volume of a sphere as
    a tuple.
    """
    # Assign the value for the constant "pi"
    PI = 3.14

    # Calculate diameter
    diameter = 2 * radius

    # Calculate circumference
    circumference = 2 * PI * radius

    # Calculate surface area
    surface_area = 4 * PI * radius**2

    # Calculate volume
    volume = (4/3) * PI * radius**3

    # Return the attributes
    return diameter, circumference, surface_area, volume