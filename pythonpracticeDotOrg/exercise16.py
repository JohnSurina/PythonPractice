# Write a password generator in Python.
# Be creative with how you generate passwords - strong
# passwords have a mix of lowercase letters, uppercase letters,
# numbers, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

# Extra:
# • Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# ----------------------------------------------------------- #

import random

lettersLower = "abcdefghijklmnopqrstuvwxyz"
lettersUpper = lettersLower.upper()
numbers = "1234567890"
symbols = "!@#$%&()[]\{\}?<>,.\\/"
randSet = lettersLower + lettersUpper + numbers + symbols

try:
    numberCharacters = int(input("Please input the number of characters you would like in your password: "))
except ValueError:
    print("please enter an actual number, cockSucker")
    exit()

returnString = ""

for i in range(0,numberCharacters):
    returnString = returnString + randSet[random.randint(0,len(randSet)-1)]

print(returnString)