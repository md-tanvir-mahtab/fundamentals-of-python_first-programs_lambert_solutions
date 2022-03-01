"""
Program: income_tax_calculator.py
Author (Motivated by the book's solution): Md. Tanvir Mahtab
Date: 2022-01-02

Purpose: This porgram contains a function for calculating income tax.
"""

# Define the function for calculating the income tax
def calculate_income_tax():
    # Initialize the constants
    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000
    DEPENDENT_DEDUCTION = 3000

    # Take the inputs
    gross_income = float(input("Enter your gross income: "))
    num_dependents = int(input("Enter the number of your dependents: "))

    # Compute the income tax
    taxable_income = gross_income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * num_dependents
    income_tax = taxable_income * TAX_RATE

    # Round the income tax at most two digits of precision
    income_tax = round(income_tax, 2)

    # Display the income tax
    print("Your income tax is $" + str(income_tax))