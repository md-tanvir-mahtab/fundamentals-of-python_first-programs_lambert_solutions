"""
Program: exercise05.py
Author: Md. Tanvir Mahtab
Date: 2022-02-08

Problem:
    What is the maximum number of guesses necessary to guess correctly a given num-
    ber between the numbers N and M?

Solution:
    >>>
"""

# Import required module(s)
import random

# Take the min and max value (inclusive) of the range
while True:
    n = int(input("Enter an integer as the minimum value (inclusive) of the range: "))
    m = int(input("Enter an integer as the maximum value (inclusive) of the range: "))

    # Check if n < m
    if n < m:
        break

# Generate a random integer (within the given range) to guess
guessable_number = random.randint(n, m)

# Initialize a variable to count guesses
guess_count = 0

# Let the user guess the number
# and check its correctness
while True:
    guess_attempt = int(input("Enter your guessed number from within your given range: "))
    guess_count += 1
    if guess_attempt == guessable_number:
        break
    else:
        print("Your guess is incorrect.")

# Display the number of guesses
print("You have guessed correctly in {} guesse(s).".format(guess_count))