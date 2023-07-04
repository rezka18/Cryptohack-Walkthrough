from Crypto.PublicKey import RSA

# Import the RSA key from a file
with open('bruce_rsa.pub', 'rb') as f:
    public_key_ssh = f.read()

public_key = RSA.import_key(public_key_ssh)
print(public_key.n)