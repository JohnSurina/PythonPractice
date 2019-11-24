# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# • Add on to the previous program by asking the user for another number
#   and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# • Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# ----------------------------------------------------------- #

import datetime

name = input("Please input your name: ")
age = int(input("Please input your age in years in: "))

today = datetime.date.today()
thisYear = today.year

if age > 100:
    yearsSinceTurned100 = age - 100
    whenTheyTurned100 = thisYear - yearsSinceTurned100
    print("wow, " + name + " you sure are old, you turned 100 in " + str(whenTheyTurned100) + "!")
else:
    yearsTill100 = 100 - age
    whenTheyWillTurn100 = thisYear + yearsTill100
    print("Hey " + name + ", you will turn 100 in the year " + str(whenTheyWillTurn100))