import hashlib
import os

file_loc=input("enter the file address:  ")

if os.path.exists(file_loc):
    with open(file_loc,"rb") as file:
        content= file.read()


hash_value= (hashlib.sha256(content)).hexdigest()
print(hash_value)