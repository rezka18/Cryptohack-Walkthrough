from base64 import b64decode

data = "PiQ"
decode = b64decode(data)

for i in range(0,256):
    decoded = "".join(chr(b ^ i) for b in decode)
    if decoded.isprintable():
        print(i, decoded)