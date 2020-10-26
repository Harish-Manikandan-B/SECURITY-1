import os
from cryptography.fernet import Fernet
file = open('h.key','rb')
key=file.read()
file.close()

input_file = 'TEST.xlsx'
output_file = 'im.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)
os.remove("TEST.xlsx")
