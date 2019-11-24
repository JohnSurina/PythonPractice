# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# ----------------------------------------------------------- #

import math

print("This script determines whether a number is even or odd. All non-integer numbers will be truncated")
mNumber = math.floor(int(input("Enter a number: ")))

if mNumber % 2 == 1:
    print(str(mNumber) + " is odd")
else:
    print(str(mNumber) + " is even", end="")

    if mNumber % 4 == 0:
        print(", your number is also a multiple of 4")
    else:
        print("")