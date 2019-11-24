# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

# ----------------------------------------------------------- #

print("This script determines if your inputted string is a palindrome")
mString = input("Please input a string: ")

isPalindrome = True
for index in range(0,len(mString)):
    if mString[index] != mString[-(index+1)]:
        isPalindrome = False
        break

if isPalindrome:
    print("Your string is a palindrome")
else:
    print("Your string is not a palindrome")