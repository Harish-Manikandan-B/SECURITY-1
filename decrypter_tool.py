import os
from cryptography.fernet import Fernet
file =open('h.key','rb')# Use one of the methods to get a key (it must be the same as used in encrypting)
key=file.read()
file.close()


input_file = 'im.encrypted'
output_file = 'TEST.xlsx'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)
#os.remove(im.encrypted)    
