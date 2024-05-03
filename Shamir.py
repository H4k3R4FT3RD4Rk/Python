from pwn import remote
from sage.all import *
from math import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from pynput import mouse

conn = remote('209.97.140.29', 31234, level = 'error')

def tesBit():
  conn.recvuntil(">")
  conn.sendline("2")
  conn.recvuntil("Input message as hex: ")
  conn.sendline("00")
  pairs = []
  for i in range(64):
    line = conn.recvline()
    pairs.append(eval(line))
  return pairs
def getFlagPairs():
  conn.recvuntil(">")
  conn.sendline("1")
  pairs = []
  for i in range(64):
    line = conn.recvline()
    pairs.append(eval(line))
  return pairs
  
## recover key
bits = [1] * 64
count_of_zero_bits = 0

while (count_of_zero_bits != 32):
  print(".")
  key_pairs = tesBit()
  for i in range(64):
    x, y = key_pairs[i]
    if ((x % 2 == 0) and (y % 2 == 1)):
      bits[i] = 0
      
  count_of_zero_bits = sum(bits)

bits.reverse()

key_bits = ""
for i in range(64):
  key_bits = key_bits + str(bits[i])
  
print("key_bits =", key_bits)

key = int(key_bits, 2)

## recover flag
flag_pairs = getFlagPairs()

R = IntegerModRing(2**1024)

x_values = []
y_values = []

for bitpos in range(64):
  if key & 1 << bitpos != 0:
    # Real
    x, y = flag_pairs[bitpos]
    
    x_list = []
    for j in range(32):
      x_list.append(x**j)
    x_values.append(x_list)
    y_values.append(y)
x_matrix = Matrix(R, x_values)
y_vector = vector(R, y_values)

poly = x_matrix.solve_right(y_vector)

print("flag = ", long_to_bytes(int(poly[0])))
