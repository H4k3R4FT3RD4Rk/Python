encrypted_message = b'\x13\x00\x1d-A*!\x00Q\x16R\x02\x12\x07\n\x1b>\x0e\x06\x1a~O-D CU\t\x0e\x06 E2\n\x17bA#\x0b\t>O\x11\x011O\tH*\x1b\x10-\x08\x00)E\x02\nMck~)\x07"\x01H*+\n_\x01\x00\x00\x00c\n\x00!\x12V\r\x1d4A\x19\x16\x0b"O!N(\x00\x13Dy\x02\x000\x08\rn\x16\x19E\x16,\x0fS\x17H+\x1c\x03N)\nEU1\x0e\x01c\x10\x1b+\x16\x02\x0c\x1d-A\x11\x15\r8\x16H\x0f#\x0e\x0cOx'
xor_key = "YouCanNeverCatchJohnDoe!"

# Convert encrypted message to string representation
encrypted_message_str = encrypted_message.decode()

# XOR decryption
decrypted_message = ""
for i in range(len(encrypted_message_str)):
    decrypted_message += chr(ord(encrypted_message_str[i]) ^ ord(xor_key[i % len(xor_key)]))

print("Decrypted Message:")
print(decrypted_message)
