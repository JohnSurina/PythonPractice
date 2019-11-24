# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
# and another number. The function decides whether or not the given number is inside the list and returns (then prints)
# an appropriate boolean.

# Extras:
# Use binary search.

#--------------------------------------------------------------------------------------------------------------------------#

import random
import math as m

def search(myArray, myValue):
    for value in myArray:
        if myValue == value:
            return(True)
    return(False)

def binarySearch(myArray, myValue):
    mArray = myArray.copy()
    mArray.sort()
    print(mArray)
    while True:
        halfPoint = m.floor(len(mArray)/2)
        print(mArray[halfPoint])
        if myValue > mArray[halfPoint]:
            mArray = mArray[halfPoint+1:len(mArray)]
            print("mArray up", mArray)
        elif myValue < mArray[halfPoint]:
            mArray = mArray[0:halfPoint]
            print("mArray down", mArray)
        elif myValue == mArray[halfPoint]:
            return(True)
        if len(mArray) == 0:
            return(False)
        if myValue != mArray[0] and len(mArray)==1:
            return(False)


array = []
for i in range(0,random.randint(10,20)):
    array.append(random.randint(0,20))

#print(array)

print(binarySearch(array, 3))