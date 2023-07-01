def gcd(a, b):
    while b != 0:
        r = a % b #sisa pembagian a dan b
        a = b 
        b = r
    return a

num1 = 66528
num2 = 52920

result = gcd(num1, num2)
print("GCD:", result)