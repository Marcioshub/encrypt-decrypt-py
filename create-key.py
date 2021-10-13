from cryptography.fernet import Fernet
# create key for encryption and decryption
key = Fernet.generate_key()
  
# save the key
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)