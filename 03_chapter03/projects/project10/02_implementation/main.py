"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-02-27

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import credit_plan

# Define the main function
def main():
    # Take input
    # Purchase price should be taken
    # as a floating-point number
    purchase_price = float(input("Enter the purchase price: "))

    # Call the function to compute
    # and display different attributes
    # of the credit status
    credit_plan.credit_status(purchase_price)

# Execution point of the program
if __name__ == "__main__":
    main()