from cryptography.fernet import Fernet
import os

def main():
    key = ""
    fernet = ""

    # read the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
        fernet = Fernet(key)

    # starting path
    path = "/Users/spency/Desktop/demo"

    # iterate through dictories starting with the path given
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            # opening the encrypted file
            with open(os.path.join(root, name), 'rb') as enc_file:
                encrypted = enc_file.read()
            # decrypting the file
            decrypted = fernet.decrypt(encrypted)
            # opening the file in write mode and
            # writing the decrypted data
            with open(os.path.join(root, name), 'wb') as dec_file:
                dec_file.write(decrypted)

if __name__=="__main__":
    main()