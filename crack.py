import hashlib
import base64
from Crypto.Cipher import AES

k = "!A%D*G-KaPdSgVkY"
code_b64 = "Tq+CWzQS0wYzs2rJ+GNrPLP6qekDbwze6fIeRRwBK2WXHOhba7WR2OGNUFKoAvyW7njTCMlQzlwIRdJvaP2iYQ=="

decoded_bytes = base64.b64decode(code_b64)
print(decoded_bytes)

cipher = AES.new(k.encode(), AES.MODE_ECB).decrypt(decoded_bytes)
print(cipher)
