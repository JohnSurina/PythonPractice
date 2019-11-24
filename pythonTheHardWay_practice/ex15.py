from sys import argv
import io

script,fileInputString = argv

try:
    fileObject = open(fileInputString)
except:
    print("invalid file path input")
    exit()

_continue = True

# initialize a reading position to a point where the 
# file should not be
mReadPosition = -1 

while(_continue):

    # read a line of text from the buffer into a string object
    # this also move the buffer position forward
    readString = fileObject.readline()

    # break if the file did not progress any after the last read
    # (meaning that you reached the end of the file)
    if mReadPosition == fileObject.tell():
        break

    # Print the string at the current position, and grab the current
    # position for comparison on the next loop (assuming no loop break)
    print(readString)
    mReadPosition = fileObject.tell()

    # Prompt the user if they want to continue reading the stream
    try:
        selector = (input("Would you like to continue? (Y/N)"))
        if selector.lower() != "y":
            _continue = False
    except:
        _continue = False

fileObject.close()
