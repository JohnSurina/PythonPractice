# Write a program (using functions!) that asks the user
# for a long string containing multiple words.
# Print back to the user the same string, except with
# the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

# ----------------------------------------------------------- #

myString = input("Input a string to have its words reversed: ")

preReverseString = myString.split()
preReverseString.reverse()
preReverseStringArray = []

for i in range(1,len(preReverseString)+1):
    if i != len(preReverseString):
        preReverseStringArray.append(preReverseString[i-1])
        preReverseStringArray.append(" ")
    else:
        preReverseStringArray.append(preReverseString[i-1])

returnString = ""
for i in preReverseStringArray:
    returnString = returnString + i
print(returnString)