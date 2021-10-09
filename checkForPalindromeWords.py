
def checkPalindrome(list):
# List to be accessed
	listOne = list

# list to store palindrome words
	palindromeList = []

	for eachElement in listOne:
		tempVar = str(eachElement)

		if tempVar.isnumeric():
			continue

		eachElementLower = tempVar.lower()

		# Reversing the string
		reverseElement = eachElementLower[::-1]

		if reverseElement == eachElementLower:
			palindromeList.append(tempVar)

	return palindromeList

if __name__=='__main__':
	listOFwords = []
	count=int(input())
    
	for i in range(count):
		listOFwords.append(input())
        
	print(checkPalindrome(listOFwords))