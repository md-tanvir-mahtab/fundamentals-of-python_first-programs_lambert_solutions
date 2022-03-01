"""
Program: credit_plan.py
Author: Md. Tanvir Mahtab
Date: 2022-02-27

Purpose: This script contains a function that can compute and display different
attributes of credit status under the credit plan of TidBit Computer Store.
"""

# Define the function
def credit_status(purchase_price):
    """
    Takes the purchase price as input, computes different attributes of credit
    status and display those.
    """
    # Specify initial value
    # of the remaining balance
    remaining_balance = purchase_price

    # Declare a variable
    # to hold the number of month
    month = 0

    # Display the header row of the table
    # Each column should be right-justified
    print("%9s%19s%20s%19s%21s%21s" % ("Month", "Current Balance", "Monthly Interest",
        "Monthly Payment", "Monthly Principal", "Remaining Balance"))
    
    # Compute and display different
    # attributes of the credit status
    while remaining_balance > 0.0:
        # Update the month
        month += 1

        # Update the current balance
        current_balance = remaining_balance

        # Compute monthly interest
        monthly_interest = current_balance * 0.12 / 12

        # Compute down payment
        down_payment = purchase_price * 0.1

        # Compute monthly payment
        monthly_payment = (purchase_price - down_payment) * 0.05

        # Compute monthly principal
        monthly_principal = monthly_payment - monthly_interest

        # Update remaining balance
        remaining_balance = current_balance - monthly_principal

        # Display the attributes
        # Each column should be right-justified
        print("%9d%19.2f%20.2f%19.2f%21.2f%21.2f" % (month, current_balance,
            monthly_interest, monthly_payment, monthly_principal, remaining_balance))