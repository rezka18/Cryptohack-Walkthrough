def mod_Inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i

print("Modular Multiplicative Inverse is ",mod_Inv(3,13))