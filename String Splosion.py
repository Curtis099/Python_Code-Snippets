string = input("Enter the string: ")
a = 1
manipulated_string = ""

while a <= len(string):
    b = 1

    while b <= a:
        manipulated_string = manipulated_string + string[b-1]
        b +=1
    a+=1

print(manipulated_string)

# Example:
# input = Code
# Output = CCoCodCode