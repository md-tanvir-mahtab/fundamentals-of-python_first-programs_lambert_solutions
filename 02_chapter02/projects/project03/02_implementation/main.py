"""
Program: main.py
Author: Md. Tanvir Mahtab
Date: 2022-01-02

Purpose: This is the main script of the project.
"""

# Import required module(s)
import rental_cost

# Define the main function
def main():
    # Take the number of new and oldie videos as input
    num_new_video = int(input("Enter the number of new videos: "))
    num_oldie_video = int(input("Enter the number of oldie videos: "))

    # Call the function for calculatng total rental cost
    total_cost = rental_cost.calculate_total_cost(num_new_video, num_oldie_video)

    # Display total cost
    print("Your total cost is $" + str(total_cost))

# Execution point of the program
if __name__ == "__main__":
    main()