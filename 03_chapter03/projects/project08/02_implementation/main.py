"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-26

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import greatest_common_divisor

# Define the main function
def main():
    # Take inputs
    while True:
        first_number = int(input("Enter a positive integer: "))
        
        # Check if the number is really positive
        if first_number > 0:
            break
        else:
            print("The number must be a positive integer.")
    
    while True:
        second_number =int(input("Enter another positive integer: "))

        # Check if the number is really positive
        if second_number > 0:
            break
        else:
            print("The number must be a positive integer.")
    
    # Specify the larger and smaller numbers
    if first_number > second_number:
        larger = first_number
        smaller = second_number
    elif first_number < second_number:
        larger = second_number
        smaller = first_number
    else:
        larger = first_number
        smaller = second_number
    
    # Call the function to compute GCD
    greatest_common_divisor.gcd(larger, smaller)


# Execution point of the program
if __name__ == "__main__":
    main()