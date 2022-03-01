"""
Program: formulas.py
Author: Md. Tanvir Mahtab
Date: 2022-01-11

Purpose: This script contains two functions that can calculate the momentum and 
kinetic energy (respectively) of an object based on its given mass and velocity.
"""

# Define the function for calculating momentum
def calculate_momentum(mass, velocity):
    """
    Takes mass and velocity of an object as inputs
    and returns its momentum.
    """

    # Return the momentum as the product of mass and velocity
    return mass * velocity


# Define the function for calculating kinetic energy
def calculate_kinetic_energy(mass, velocity):
    """
    Takes mass and velocity of an object as inputs
    and returns its kinetic energy.
    """

    # Return the kinetic energy as per the formula KE = (1/2) * mass * (velocity)^2
    return (1/2) * mass * (velocity)**2