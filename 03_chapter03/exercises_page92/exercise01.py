"""
Program: exercise01.py
Author: Md. Tanvir Mahtab
Date: 2022-02-07

Problem:
    Translate the following for loops to equivalent while loops:
    a. for count in range(100):
            print(count)
    b. for count in range(1, 101):
            print(count)
    c. for count in range(100, 0, -1):
            print(count)

Solution:
    >>>
"""

# Solution of (a)

# Initialize the count variable
count = 0

# Equivalent "while" loop
while count<100:
    print(count)
    count += 1

print("----------------------------------")


# Soltion of (b)

# Initialize the count variable
count = 1

# Equivalent "while" loop
while count<101:
    print(count)
    count += 1

print("----------------------------------")


# Solution of (c)

# Initialize the count variable
count = 100

# Equivalent "while" loop
while count>0:
    print(count)
    count -= 1