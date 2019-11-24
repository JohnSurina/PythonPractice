# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# ----------------------------------------------------------- #

import random

userGuess = input("Try and guess an integer between 1 and 9 (inclusive): ")

try:
    userGuessParsed = int(userGuess)
except ValueError:
    print("Input invalid")
    exit()

if userGuessParsed == random.randint(1,9):
    print("You guessed correctly!")
else:
    print("Sorry, you guessed incorrectly.")