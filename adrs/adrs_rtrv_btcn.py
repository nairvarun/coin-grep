import base64
import os
from cryptography.fernet import Fernet

process = input("select encryption (E) or decryption (D)? ")

if process == "E":
    message = input("Enter the message for encryption: ").encode()

    password = input("Enter the password: ").encode()
    key = os.urandom 
    key = base64.urlsafe_b64encode(password)

    cipher = Fernet(key)
    cipher_text = cipher.encrypt(message)

    file_name = input("Enter the file name to store the encrypted message: ")
    with open(file_name, "wb") as file:
        file.write(cipher_text)

elif process == "D":
    file_name = input("Enter the file name with the encrypted message: ")
    with open(file_name, "rb") as file:
        cipher_text = file.read()

    password = input("Enter the password: ").encode()

    key = base64.urlsafe_b64encode.encode()

    cipher = Fernet(key)
    plain_text = cipher.decrypt(cipher_text)

    print("Decrypted Message:", plain_text.decode())
else:
    print("Invalid process choice. Please choose either 'E' for encryption or 'D' for decryption.")
