# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place,
# they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

#------------------------------------------------------------------------------------------------------#

import random

print("","Cow and Bulls.",
      "Try and guess the 4 digit randomly generated number.",
      "For every digit in the correct place, you earn a \"cow\"",
      "For every correct digit in the wrong place, you get a bull.", sep="\n")

myNumber = [
            random.randint(0,9),
            random.randint(0,9),
            random.randint(0,9),
            random.randint(0,9),
           ]

print("")

totalcow = 0
totalbull = 0
won = False

while not won:
    cow = 0
    bull = 0
    userInput = input("guess a number: ")
    isANumber = userInput.isnumeric()
    myNumberCopy = myNumber.copy()
    if len(userInput) != 4 or not isANumber:
        print("please input a 4 digit number")
        continue

    userInputIterator = []
    for gamma in userInput:
        userInputIterator.append(int(gamma))

    if userInputIterator == myNumber:
        won = True
        continue

    numbersToRemove = []
    for alpha in range(0,4):
        if userInputIterator[alpha] == myNumber[alpha]:
            cow = cow + 1
            numbersToRemove.append(alpha)
    numbersToRemove.sort(reverse=True)
    for beta in numbersToRemove:
        userInputIterator.pop(beta)
        myNumberCopy.pop(beta)
    for omega in myNumberCopy:
        if omega in userInputIterator:
            bull = bull + 1
            userInputIterator.pop(userInputIterator.index(omega))

    print("Not quite.\n",
          "Cows: {0}\nBulls: {1}".format(cow,bull),
          end="\n\n")
    totalcow = totalcow + cow
    totalbull = totalbull + bull

print("You Won!",
        "Cows: {0}".format(totalcow),
        "Bulls: {0}".format(totalbull),
        sep="\n")

