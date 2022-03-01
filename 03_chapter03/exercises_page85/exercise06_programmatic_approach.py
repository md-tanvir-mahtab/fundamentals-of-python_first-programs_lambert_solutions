"""
Program: exercise06_programmatic_approach.py
Author: Md. Tanvir Mahtab
Date: 2022-02-04

Problem:
    Construct truth tables for the following Boolean expressions:
    a. not (A or B)
    b. not A and not B

Solution:
    >>>
"""

# Solution of (a)
print('--------------- Truth table for "not (A or B)"-------------')
print()

# Display the header row for the table
print("%8s%8s%12s%16s" % ("A", "B", "A or B", "not (A or B)"))

# Construct and display the truth table
for a in [False, True]:
    for b in [False, True]:
        print("%8s%8s%12s%16s" % (a, b, a or b, not (a or b)))

print()
print()

# Solution of (b)
print('--------------- Truth table for "not A and not B"-------------')
print()

# Display the header row for the table
print("%8s%8s%12s%12s%22s" % ("A", "B", "not A", "not B", "not A and not B"))

# Construct and display the truth table
for a in [False, True]:
    for b in [False, True]:
        print("%8s%8s%12s%12s%22s" % (a, b, not a, not b, not a and not b))