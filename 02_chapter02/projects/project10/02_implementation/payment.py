"""
Program: payment.py
Author: Md. Tanvir Mahtab
Date: 2022-01-13

Purpose: This script contains a function that can calculate the total weekly pay of
an employee based on his/her hourly wage, total regular hours, and total overtime hours.
"""


# Define the function to calculate total weekly pay
def total_weekly_pay(hourly_wage, total_regular_hours, total_overtime_hours):
    """
    Takes hourly wage, total regular hours, and total overtime hours as inputs and
    returns total weekly pay.
    """

    # Calculate total overtime pay
    total_overtime_pay = total_overtime_hours * (1.5 * hourly_wage)

    # Calculate and return total weekly pay
    return hourly_wage * total_regular_hours + total_overtime_pay