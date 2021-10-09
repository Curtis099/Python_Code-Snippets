# Function to reverse the string
def FirstReverse(strParam):
    lengthOfStr = len(strParam)
    reversedString = ""
    i = 0

    while i < lengthOfStr:
        reversedString = reversedString + strParam[lengthOfStr-i-1]
        i += 1

    return reversedString

# Option 2:
def SecondReverse(strParam):
    reversedString = strParam[::-1]
    return reversedString

print(FirstReverse("I Love Coding"))
print(SecondReverse("I Love Coding"))