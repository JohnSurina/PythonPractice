def Add(*addTerms):
    returnMe = float(0);
    for element in addTerms:
        returnMe = returnMe + element
    return returnMe

# Test
print(Add(1,2,3,4,5))

print(__name__)