"""
Program: exercise05.py
Author: Md. Tanvir Mahtab
Date: 2022-02-03

Problem:
    Explain how to check for an invalid input number and prevent it being used in a
    program. You may assume that the user enters a number.

Solution:
    Let's consider a fictitious scenario where a user has to input a (any) four-digit 
    number in order to get access to a system. The code is given below.
"""

# Take a four-digit number as input
access_number = int(input("Enter any four digit number: "))

# Give/deny access by checking the validity of the input
while len(str(access_number)) != 4:
    print("Access denied.\nThe input is not a four-digit number.")

    # Take the correct input
    access_number = int(input("Enter any four-digit number: "))
else:
    print("Access granted.")