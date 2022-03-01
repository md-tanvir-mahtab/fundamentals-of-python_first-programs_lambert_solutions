"""
Program: lucky_sevens.py
Author: Md. Tanvir Mahtab
Date: 2022-03-01

Purpose: This script contains a function that can compute and display the status of the 
lucky sevens game.
"""

# Import required module(s)
import random

# Define the function
def show_game_status(money):
    """
    Takes the amount of money as input, computes the status of the game, and display it.
    """
    # Declare a variable
    # to hold the number of rolls
    rolls = 0

    # Declare a variable
    # to hold the maximum amount of money
    max_money = 0.0

    # Play the game
    # until the pot of money is empty
    while money > 0:
        # Update the number of rolls
        rolls += 1

        # Get the score for each dice
        first_dice_score = random.randint(1, 6)
        second_dice_score = random.randint(1, 6)

        # Decide the result and get feedback
        if first_dice_score + second_dice_score == 7:
            # Get the reward
            money += 4

            # Update the maximum amount of money
            if money > max_money:
                max_money = money
        else:
            # Get the punishment
            money -= 1

            # Update the maximum amount of money
            if money > max_money:
                max_money = money
    
    # Display the total number of rolls
    # and the maximum amount of money
    print("Total number of rolls:", rolls)
    print("Maximum amount of money:", max_money)