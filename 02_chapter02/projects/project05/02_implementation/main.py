"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-11

Purpose: This is the main script of the project.
"""


# Import required module(s)
import momentum


# Define the main function
def main():
    # Take the mass of the object (in Kilograms) as input
    mass = float(input("Enter the mass of the object (in Kilograms): "))

    # Take the velocity of the object (in meters per second) as input
    velocity = float(input("Enter the velocity of the object (in meters per second): "))

    # Call the function for calculating momentum
    object_momentum = momentum.calculate_momentum(mass, velocity)

    # Print the momentum
    print("The momentum of the object is", object_momentum, "Kgm/s")


# Execution point of the program
if __name__ == "__main__":
    main()