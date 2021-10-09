# Initializing a vavriable with type 'List'.
numbers = list()

#Taking operator input for the user.
operator = input("Enter:  'A' for Addition\n\t'S' for Subtraction\n\t'M' for Multiplication\n\t'D' for Division\n")    

while True:
    # Taking input from the user.
    inputNum = input("Enter the number/s: ")
    if inputNum == 'Done': break

    try:
        # Converting the input to 'float'.
        inputNum = float(inputNum)
    except:
        print("Enter valid Number")
        continue

    # Inserting the number in the list
    numbers.append(inputNum)


def addition():
    add = sum(numbers)
    return add

if operator == 'A':
    print("Addition Total: ",addition())
elif operator == 'S':
    # Sorting the list with reverese order,i.e. Largest first, smallest last.
    numbers.sort(reverse=True)
    stotal = 0
    for eachNumber in numbers:
        if stotal == 0:
            stotal = eachNumber
            continue
        stotal = stotal-eachNumber
    
    print("Subtraction Total: ",stotal)
elif operator == 'M':
    mtotal = 1
    for eachNumber in numbers:
        mtotal = mtotal*eachNumber
    
    print("Multiplication Total: ",mtotal)
elif operator == 'D':
    numbers.sort(reverse=True)
    dtotal = 1
    for eachNumber in numbers:
        if dtotal == 1:
            dtotal = eachNumber
            continue
        dtotal = dtotal/eachNumber
    
    print("Division Total: ",dtotal)
else:
    print("Invalid Input while choosing the operator.")