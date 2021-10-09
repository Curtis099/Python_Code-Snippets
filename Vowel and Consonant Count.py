string = "Welcome123"
a = 0
lengthOfString = len(string)
vowelCount = 0
consonantCount = 0

while a < lengthOfString:
    try:
        # Checking if the letter is a number, and if yes, then just passs
        numericValue = int(string[a])
    except:
        # To check if the letter is vowel or not
        if string[a] == 'a' or string[a] == 'e' or string[a] == 'i' or string[a] == 'o' or string[a] == 'u' or string[a] == 'A' or string[a] == 'E' or string[a] == 'I' or string[a] == 'O' or string[a] == 'U':
            vowelCount = vowelCount + 1
        else:
            consonantCount = consonantCount + 1
    a += 1

print("Vowel Count:", vowelCount)
print("consonant Count:", consonantCount)

