def longestWordInAString(str):

    str = "I love cats"
    # To remove any special characters present in the string and to form a list
    strList = str.split()
    print(strList)
    longestWord = ""

    # To refine if the word is an alphabet or a digit
    for eachElement in strList:
        if eachElement.isalpha() or eachElement.isdigit():
            longestWord = longestWord + " " + eachElement
        else:
            longestWord = " "

    return max(longestWord.split(), key=len)

print(longestWordInAString("I Love cats"))