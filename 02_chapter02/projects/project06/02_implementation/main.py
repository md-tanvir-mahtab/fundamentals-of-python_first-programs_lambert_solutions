"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-11

Purpose: This is the main script of the project.
"""


# Import required module(s)
import formulas


# Define the main function
def main():
    # Take the mass of the object (in Kilograms) as input
    mass = float(input("Enter the mass of the object (in Kilograms): "))

    # Take the velocity of the object (in meters per second) as input
    velocity = float(input("Enter the velocity of the object (in meters per second): "))

    # Call the function for calculating momentum
    momentum = formulas.calculate_momentum(mass, velocity)

    # Call the function for calculating kinetic energy
    kinetic_energy = formulas.calculate_kinetic_energy(mass, velocity)

    # Print the momentum
    print("The momentum of the object is", momentum, "Kgm/s")

    # Print the kinetic energy
    print("The kinetic energy of the object is", kinetic_energy, "Joule(s)")


# Execution point of the program
if __name__ == "__main__":
    main()