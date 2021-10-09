# List to be Accessed
listOfStrings = ['customer', 'ksjdy', 'llll']

# Empty list to store non vowel words
noVowelsList = []
    
for eachString in listOfStrings:
	tempVar = str(eachString)
	elementLower = tempVar.lower()
	print(elementLower)
	lenOfElement = len(elementLower)
	i = 0
	while i < lenOfElement:

		if elementLower[i] == 'a' or elementLower[i] == 'e' or elementLower[i] == 'i' or elementLower[i] == 'o' or elementLower[i] == 'u':
			break
		else:
			if lenOfElement-i == 1:
				noVowelsList.append(elementLower)
			i += 1

print(noVowelsList)

            