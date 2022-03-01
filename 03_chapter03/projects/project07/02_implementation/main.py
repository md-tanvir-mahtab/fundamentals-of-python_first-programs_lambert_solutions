"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-14

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import salary

# Define the main function
def main():
    # Take inputs
    starting_salary = float(input("Enter the starting salary: "))
    percentage_increase = float(input("Enter the percentage increase: "))
    # Convert percentage to decimal
    percentage_increase /= 100
    years = int(input("Enter the number of years: "))

    # Call the function to calculate
    # and display salaries
    salary.calculate_salary(starting_salary, percentage_increase, years)

# Execution point of the program
if __name__ == "__main__":
    main()