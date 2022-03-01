"""
Program: population.py
Author: Md. Tanvir Mahtab
Date: 2022-02-12

Purpose: This script contains a function that can calculate the final population of a 
particular organism based on its initial population, growth rate, growth period, and 
total time of growth.
"""

# Define the function
def calculate_final_population(population, growth_rate, growth_period, total_time):
    """
    Takes initial population, growth rate, growth period, and total time of growth 
    as inputs; calclates the final population and returns it.
    """
    # Compute the number of full growth times
    full_growth_times = total_time // growth_period

    # Compute population after full growth times
    while full_growth_times > 0:
        population = population * growth_rate
        full_growth_times -= 1
    
    # Compute partial growth time
    partial_growth_time = total_time % growth_period

    # Compute population at partial growth time
    partial_population = population * (partial_growth_time / growth_period)

    # Return the final population
    return population + partial_population