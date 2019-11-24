# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

# ----------------------------------------------------------- #

import math

def isNumberPrime(input):
    try:
        mNumber = math.floor(int(input))
    except:
        print("An Exception Occured")
        return(None)

    divisorArray = []

    for alpha in range(2,mNumber):
        if mNumber % alpha == 0:
            divisorArray.append(alpha)

    if len(divisorArray) == 0:
        return(True)
    else:
        return(False)

print("This script determines if a number is prime or not")
userInput = input("Input number: ")

if isNumberPrime3(userInput):
    print("Number is prime")
else:
    print("Number is not prime")