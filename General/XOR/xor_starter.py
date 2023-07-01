var1 = "label"
var2 = 13

ord = [ord(c) for c in var1]
xor = [13 ^ i for i in ord]
xor_string = ["".join(chr(o) for o in xor)]

print(ord)
print(xor_string)