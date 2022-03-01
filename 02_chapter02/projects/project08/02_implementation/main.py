"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-13

Purpose: This is the main script of the project.
"""


# Import required module(s)
import distance


# Define the main function
def main():
    # Call the function to calculate light-year
    val_light_year = distance.light_year()

    # Display the result
    print("One light-year =", val_light_year, "meters")


# Execution point of the program
if __name__ == "__main__":
    main()