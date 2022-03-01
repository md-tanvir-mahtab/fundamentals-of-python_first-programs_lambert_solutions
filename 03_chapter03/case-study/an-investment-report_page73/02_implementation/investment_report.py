"""
Program: investment_report.py
Author (Motivated by the book's author): Md. Tanvir Mahtab
Date: 2022-02-02

Purpose: This script contains a function that computes different investment metrics 
and displays those as a report.
"""

# Define the function
def get_investment_report():
    """
    Computes Year, Starting balance, Interest, Ending balance, and total interest and
    displays those as a report.
    """
    
    # Recieve the user inputs and initialize data
    # The starting balance should be a floating-point number
    start_balance = float(input("Enter the starting balance: "))
    
    # The number of years should be an integer
    years = int(input("Enter the number of years: "))

    # The rate of interest should be a percentage expressed as an integer
    rate = int(input("Enter the rate of interest as a %: "))

    # Convert the rate into a decimal number
    rate = rate/100

    # Initialize the total interest
    total_interest = 0.0

    # Display the header of the table
    print("%4s%18s%10s%16s" % \
    ("Year", "Starting balance", "interest", "Ending balance"))

    # Compute and dislay the results for each year
    for year in range(1, years+1):
        # Compute the interest
        interest = start_balance * rate

        # Compute the ending balance
        end_balance = start_balance + interest

        # Display the year, starting balance, interest, and ending balance
        print("%4d%18.2f%10.2f%16.2f" % \
        (year, start_balance, interest, end_balance))

        # Update the starting balance
        start_balance = end_balance

        # Update the total interest
        total_interest += interest
    
    # Display the totals for the period
    print("Ending balance: $%0.2f" % end_balance)
    print("Total interest earned: $%0.2f" % total_interest)