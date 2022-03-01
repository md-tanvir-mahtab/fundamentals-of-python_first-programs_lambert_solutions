"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-03-01

Purpose: This script contains the main function of the project.
"""

# Import required module(s)
import lucky_sevens

# Define the main function
def main():
    # Take input
    # The amount of money should be
    # taken as a floating-point number
    money = float(input("Enter the amount of money ($): "))

    # Call the function to play the game
    # and get its status
    lucky_sevens.show_game_status(money)


# Execution point of the program
if __name__ == "__main__":
    main()