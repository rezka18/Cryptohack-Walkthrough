data = "191466a2d1f1115263e5b56105d216e7420123b95c5f37401876257e3223733e66251e1d5f39156b3a3c"
data = bytes.fromhex(data)

flag_format = b"hacklabs{"
key = [i1 ^ i2 for (i1, i2) in zip(data, flag_format)] + [ord("y")]

flag = []
key_len = len(key)
for i in range(len(data)):
    flag.append(data[i] ^ key[i % key_len])

flag = "".join(chr(o) for o in flag)

print(flag)