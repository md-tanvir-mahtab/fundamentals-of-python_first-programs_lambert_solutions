"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-12

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import population

# Define the main function
def main():
    # Take inputs
    initial_population = int(input("Enter the initial population: "))
    growth_rate = float(input("Enter the growth rate: "))
    growth_period = float(input("Enter the growth period (in hours): "))
    total_time = float(input("Enter the total time (in hours): "))

    # Call the function to calculate
    # the final population
    final_population = population.calculate_final_population(initial_population, growth_rate, growth_period, total_time)

    # Display the final population
    print("The final population will be", final_population)

# Execution point of the program
if __name__ == "__main__":
    main()