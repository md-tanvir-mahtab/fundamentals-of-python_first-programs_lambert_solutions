"""
================================ Basic Info ===========================================
Program: case-study_income-tax-calculator.py
Author (Motivated by the book's solution): Md. Tanvir Mahtab
Date: 2021-11-28

================================ Problem (Customer request) ============================
Write a program that computes a person's income tax.

================================ Analysis ==============================================
In order to write the program we need some information about the relevant tax law.
For the sake of simplicity, let’s assume the following tax laws:
    • All taxpayers are charged a flat tax rate of 20%.
    • All taxpayers are allowed a $10,000 standard deduction.
    • For each dependent, a taxpayer is allowed an additional $3,000 deduction.
    • Gross income must be entered to the nearest penny.
    • The income tax is expressed as a decimal number.

We also need to know what information the user will have to provide.
In this case, the user inputs are gross income and number of dependents. The
program calculates the income tax based on the inputs and the tax law and then
displays the income tax.

================================ Design ================================================
During analysis, we specify what a program is going to do. In the next phase, design,
we describe how the program is going to do it. This usually involves writing an algo-
rithm, typically in the form of a pseudocode.
Here is the pseudocode for our income tax program:
    -> Input the gross income and number of dependents
    -> Compute the taxable income using the formula
        Taxable income = gross income - 10000 - (3000 * number of dependents)
    -> Compute the income tax using the formula
        Tax = taxable income * 0.20
    -> Print the tax

We can also express this pseudocode as a function and make it more similar to the actual Python 
code as follows:

FUNCTION calculate_income_tax()
    # Initialize the constants
    CONSTANT tax_rate = 0.20
    CONSTANT standard_deduction = 10000
    CONSTANT dependent_deduction = 3000

    # Take the inputs
    gross_income = INPUT("Enter your gross income: ")
    num_dependents = INPUT("Enter the number of dependents: ")

    # Compute the income tax
    taxable_income = gross_income - standard_deduction - dependent_deduction * num_dependents
    income_tax = taxable_income * tax_rate

    # Output the income tax
    OUTPUT income_tax
END FUNCTION

============================= Implementation (Coding) ============================
>>>
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

    # Display the income tax
    print("Your income tax is $" + str(income_tax))

# Define the main function
def main():
    calculate_income_tax()

# Execution point of the program
if __name__ == "__main__":
    main()