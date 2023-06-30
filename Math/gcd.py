def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)

a = 66528
b = 52920

# prints result
print ("The gcd is : ",end="")
print (computeGCD(a, b))