# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the 
# elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t
# figure this out at this point - we’ll get to it soon)

# ----------------------------------------------------------- #

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# print("This script finds the overlapping elements of two lists")

# a_cp = a.copy()
# b_cp = b.copy()

# def removeCopies(list_):
#     for element in list_:
#         while list_.count(element) > 1:
#             list_.remove(element)

# removeCopies(a_cp)
# removeCopies(a_cp)

# returnList = []

# for element in a_cp:
#     if b_cp.count(element):
#         returnList.append(element)

# print(returnList)

# ----------------------------------------------------------- #

import math
import random

def generateRandomIntList():
    mList = []
    for i in range(1,random.randint(5,20)):
        mList.append(random.randint(1,10))
    return(mList)

a = generateRandomIntList(); print(a)
b = generateRandomIntList(); print(b)

print("This script finds the overlapping elements of the two randomly generated lists above")

a_cp = a.copy()
b_cp = b.copy()

def removeCopies(list_):
    for element in list_:
        while list_.count(element) > 1:
            list_.remove(element)

removeCopies(a_cp)
removeCopies(a_cp)

returnList = []

for element in a_cp:
    if b_cp.count(element):
        returnList.append(element)

print(returnList)