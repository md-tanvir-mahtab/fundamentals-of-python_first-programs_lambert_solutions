"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-13

Purpose: This is the main script of the project.
"""

# Import required module(s)
import minutes


# Define the main function
def main():
    # Call the function to calculate the number of minutes in a year
    num_minutes = minutes.minutes_in_a_year()

    # Print the result
    print("There are", num_minutes, "minutes in a year.")


# Execution point of the program
if __name__ == "__main__":
    main()