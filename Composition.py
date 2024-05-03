from pwn import *
from ecc import Point
from sympy.ntheory.primetest import is_square
from sympy import sqrt
from Crypto.Util.Padding import unpad
from Crypto.Util.number import isPrime
from Crypto.Cipher import AES
from hashlib import md5

# attempt to factorize n using fermat factorization
def fermat_factorize(n, bound = 10**6):
	i = 1
	p, q = None, None
	for i in range(bound):
		num = n + i**2
		if is_square(num):
			root = sqrt(num)
			p = root - i
			q = root + i
			break
	return (p,q)

# get the values for a and b given two points on the curve
def get_curve_constants(p1, p2, n):
	a = moddiv((p2.y**2 - p1.y**2 - p2.x**3 + p1.x**3), (p2.x - p1.x), n)
	b = p1.y**2 - p1.x**3 - a*p1.x

	return (a % n, b % n)

def decryption(g, iv, ct):
	key = md5(str(g.x).encode()).digest()
	iv = bytes.fromhex(iv)
	cipher = AES.new(key, AES.MODE_CBC, iv)

	return cipher.decrypt(bytes.fromhex(ct))

# Copied from server.py
def next_prime(num):
    if num % 2 == 0:
        num += 1
    else:
        num += 2
    while not isPrime(num):
        num += 2
    return num

# handles getting the output from the remote server
def get_variables(host, port):
	r = remote(host, port)
	p = log.progress('Recieving data')

	r.recvuntil('Encrypted flag: ')
	flag = r.recvline().decode().strip()
	iv = r.recvline().decode().split(' ')[1].strip()
	n = r.recvline().decode().split(' ')[1].strip()
	pointA = r.recvline().decode().split(' ')
	A = Point(int(pointA[2][8:-1]), int(pointA[3][2:-2]))

	r.recvuntil('[y/n]> ')
	r.writeline('y')
	r.recvuntil('point...')
	r.recvline()
	pointG = r.recvline().decode().split(' ')
	G = Point(int(pointG[0][8:-1]), int(pointG[1][2:-2]))
	p.success('recieved')

	return (flag, iv, int(n), A, G)

HOST = '209.97.140.29'
PORT =30079

# get values from server
encrypted_flag, iv, N, A, randG = get_variables(HOST, PORT)

#calculate variables
a, b = get_curve_constants(A, randG, N)
p, q = fermat_factorize(N)
e = next_prime(int(p) >> 128) # p is a sympy.core.numbers.Integer

# output variables so we can input them in sagemath
print(f"p: {p}")
print(f"q: {q}")
print(f"a: {a}")
print(F"b: {b}")

# get these values from the output of https://sagecell.sagemath.org/
order_Ep = int(input('Enter the order of the curve Ep: '))
order_Eq = int(input('Enter the order of the curve Eq: '))

# calculate our inverses
e_inv_order_Ep = pow(e, -1, order_Ep)
e_inv_order_Eq = pow(e, -1, order_Eq)

# construct the seperate curves mod p and q
Ep = EllipticCurve(a, b, p)
Eq = EllipticCurve(a, b, q)

# create the point on each curve
A_Ep = Point(A.x % p, A.y % p)
A_Eq = Point(A.x % q, A.y % q)

# Multiply by inverse on each curve
g_Ep = Ep.multiply(A_Ep, e_inv_order_Ep)
g_Eq = Eq.multiply(A_Eq, e_inv_order_Eq)

# combine to a point over N
g_Epq = Point(crt([g_Ep.x, p], [g_Eq.x, q]), crt([g_Ep.y, p], [g_Eq.y, q]))

# decrypt
flag = unpad(decryption(g_Epq, iv, encrypted_flag))

print(flag.decode())
