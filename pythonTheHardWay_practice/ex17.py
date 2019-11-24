# to test (from enclosing dir, assuming cpFrom exists):
# python3 ./ex17.py ./ex17_cpFrom.txt ./ex17_cpTo.txt

# This file emulates bash's cp function
import os.path
import sys

[script,fromFile,toFile] = sys.argv

existsFrom = os.path.exists(fromFile)
existsTo = os.path.exists(toFile)

if existsFrom:
    print("Copied file existance confirmed")
    print("Confirm file to copy: {0}".format(fromFile),end="")
    confirm = input(" ?(y/n): ")
    if confirm.lower() != "y":
        exit()
else:
    exit()
if existsTo:
    confirm = input("Are you sure you want to overwrite {0} ?(y/n):".format(toFile))
    if confirm.lower() != "y":
        exit()

fromFileText = open(fromFile).read()
open(toFile,"w").write(fromFileText)