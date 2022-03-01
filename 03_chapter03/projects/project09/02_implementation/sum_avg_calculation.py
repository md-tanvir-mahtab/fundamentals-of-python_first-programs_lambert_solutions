"""
Program: sum_avg_calculation.py
Author: Md. Tanvir Mahtab
Date: 2022-02-27

Purpose: This script contains a function that can calculate the sum and average of a
series of numbers and display the results.
"""

# Define the function
def sum_and_average():
    # Declare a variable
    # to count the input numbers
    count = 0

    # Declare a variable
    # to hold the sum of input numbers
    the_sum = 0

    # Declare a variable
    # to hold the average of input numbers
    the_average = 0

    # Take inputs
    # and compute the sum and average
    while True:
        response = input("Enter a number or press the Enter/Return key to get the results: ")
        
        # Pressing only the Enter/Return key
        # is equivalent to inputting an empty string
        if response == "":
            break
        else:
            # Update the count of the number
            count += 1
            
            # Convert the response
            # to a floating-point number
            number = float(response)

            # Update the sum and average
            the_sum += number
            the_average = the_sum / count
    
    # Display the sum and average
    print("The sum is:", the_sum)
    print("The average is:", the_average)