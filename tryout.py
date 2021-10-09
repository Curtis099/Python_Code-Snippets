def checkPassword(string):
    if len(str) < 4:
        return 0

    a = 0
    # Check for At least One Numeric Digit in it.
    for eachLetter in string: # Needs too be changed
        try:
            num = int(string[a])
            break
        except:
            if a == (len(string)-1): return 0

            a += 1
            continue

    # Check for Capital letter
    tempStr = str(string)
    tempStr.lower()

    if tempStr == string:
        return 0
    else:
        pass


