from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import base64
 
# Encrypted data, password, and salt
encrypted_data = base64.b64decode("FOqxc90aMQZydCQb2MUm5tj4kRIxxVeCDWzAANfOrr8JItHYneUHhSV0awvQIo/8E1LtfYm/+VVWz0PDK6MXp38BWHoFDorhdS44DzYj9CQ=")
password = "aesiseasy"
salt = base64.b64decode("c2FsdHZhbA==>")
 
# Derive key and IV using PBKDF2
key = PBKDF2(password, salt, dkLen=32, count=100000)  # 256-bit key
iv = get_random_bytes(16)  # 128-bit IV
 
# Initialize AES decryption
cipher = AES.new(key, AES.MODE_CBC, iv)
 
# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)
 
# Print the decrypted data
print(decrypted_data.decode('utf-8'))
 
