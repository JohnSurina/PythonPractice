# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# • Add on to the previous program by asking the user for another number
#   and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# • Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# ----------------------------------------------------------- #

import datetime

print("")
print("This program will tell you when you will turn 100 years old.")
usersName = input("What is your name?: ")
usersAge = input("what is your age?: ")

yearsUntil100 = 100 - int(usersAge)

today = datetime.date.today()
currentYear = today.year

yearUserTurns100 = currentYear + yearsUntil100

print("Hey {0}, you will turn 100 years in the year: {1}".format(usersName, yearUserTurns100))