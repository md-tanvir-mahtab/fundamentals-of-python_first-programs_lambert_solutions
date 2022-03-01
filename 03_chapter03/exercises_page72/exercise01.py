"""
Program: exercise01.py
Author: Md. Tanvir Mahtab
Date: 2022-01-27

Problem:
    Assume that the variable amount refers to 24.325. Write the outputs of the following
    statements:
    a. print("Your salary is $%0.2f" % amount)
    b. print("The area is %0.1f" % amount)
    c. print("%7f" % amount)

Solution:
    a. Your salary is $24.32
    b. The area is 24.3
    c. 24.325000

"""

# Initialize the variable "amount"
amount = 24.325

# Statement of (a)
print("Your salary is $%0.2f" % amount)

# Statement of (b)
print("The area is %0.1f" % amount)

# Statement of (c)
print("%7f" % amount)