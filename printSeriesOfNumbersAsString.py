# To print a series of numbers as a string.

n = int(input('N: '))
k = 1
string = ''
while (k<=n):
    string = string + str(n-(n-k))
    k += 1

print(string)