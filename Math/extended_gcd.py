def gcd(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)

p = 26513
q = 32321

print(gcd(p, q))