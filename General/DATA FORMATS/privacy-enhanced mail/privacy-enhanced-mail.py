from Crypto.PublicKey import RSA

f = open('privacy_enhanced_mail.pem', 'r')
key = RSA.import_key(f.read())
print(key.d) #decrypt property