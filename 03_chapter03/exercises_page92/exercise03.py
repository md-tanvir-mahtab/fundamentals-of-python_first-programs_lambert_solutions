"""
Program: exercise03.py
Author: Md. Tanvir Mahtab
Date: 2022-02-07

Problem:
    The log2 of a given number N is given by M in the equation N = 2^M . Using integer
    arithmetic, the value of M is approximately equal to the number of times N can be
    evenly divided by 2 until it becomes 0. Write a loop that computes this approxima-
    tion of the log2 of a given number N. You can check your code by importing the
    math.log function and evaluating the expression round(math.log(N, 2)) (note
    that the math.log function returns a floating-point value).

Solution:
    >>>
"""

# Take input
while True:
    number = int(input("Enter a positive integer to get its base-2 log: "))
    
    # Check if the input is a positive integer
    if number == abs(number) and number != 0:
        break

# Keep a copy of the given number
given_number = number

# Initialize the counter
# whose value would be considered as the base-2 log
# of the given number
count = -1

# Compute the log2
while number > 0:
    count += 1

    # Update the number
    number = number//2

print("The base-2 log (approx.) of {} is {}".format(given_number, count))

print("------------------ Testing ----------------")
import math
print("The rounded answer given by the built-in 'log' function is",
    round(math.log(given_number, 2)))