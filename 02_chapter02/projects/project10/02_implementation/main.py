"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-13

Purpose: This is the main script of the project.
"""


# Import required module(s)
import payment


# Define the main function
def main():
    # Take hourly wage as input
    hourly_wage = float(input("Enter the hourly wage ($): "))

    # Take total regular hours as input
    total_regular_hours = float(input("Enter total regular hours: "))

    # Take total overtime hours as input
    total_overtime_hours = float(input("Enter total overtime hours: "))

    # Call the function to calculate total weekly pay
    weekly_pay = payment.total_weekly_pay(hourly_wage, total_regular_hours, total_overtime_hours)

    # Display the total weekly pay
    print("Your total weekly pay is $" + str(round(weekly_pay, 2)))


# Execution point of the program
if __name__ == "__main__":
    main()