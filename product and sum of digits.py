# Function to find the product and sum of each digit of a given number 
def productAndSum(n):
    a = 0
    product = 1
    sum = 0
    strOfN = str(n)

    while a < len(strOfN):
        product  = product*int(strOfN[a])
        sum = sum + int(strOfN[a])
        diff = product-sum
        a += 1

    return diff

print(productAndSum(234))