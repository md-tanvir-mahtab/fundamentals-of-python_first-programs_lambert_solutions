"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-13

Purpose: This is the main script of the project.
"""


# Import required module(s)
import conversion


# Define the main function
def main():
    # Take number of kilometers as input
    kilometers = float(input("Enter the number of kilometers: "))

    # Call the function to convert kilometers to nautical miles
    nautical_miles = conversion.km_to_nm(kilometers)

    # Display the result
    print("{} kilometer(s) = {} nautical mile(s).".format(kilometers, nautical_miles))


# Execution point of the program
if __name__ == "__main__":
    main()