"""
Program: salary.py
Author: Md. Tanvir Mahtab
Date: 2022-02-14

Purpose: This script contains a function that can calculate and display salaries for 
each of the the given years in a tabular format.
"""

# Define the function
def calculate_salary(salary, percentage_increase, years):
    """
    Takes starting salary, percentage increase, and years as arguments; calculates 
    salaries and displays them year-wise in a tabular format.
    """
    # Display the header row of the table
    # Make each column right-aligned
    print("%5s%14s" % ("Year", "Salary"))

    # Calculate and display salaries
    for year in range (1, years+1):
        # Make each column right-aligned
        print("%5d%14.2f" % (year, salary))

        # Calculate salary for the next year
        salary += salary * percentage_increase