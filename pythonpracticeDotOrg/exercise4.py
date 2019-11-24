# Create a program that asks the user for a number and then prints
# out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that 
# divides evenly into another number. For example,
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

# ----------------------------------------------------------- #

import math

print("This script finds all divisors of a given (truncated) positive number")
mNumber = math.floor(int(input("Please input your number: ")))

print("divisors: [", end="")
for alpha in range(1,mNumber+1):
    if mNumber == alpha:
        print(alpha, end="")
        continue
    elif mNumber % alpha == 0:
        print(alpha, end=", ")
print("]")