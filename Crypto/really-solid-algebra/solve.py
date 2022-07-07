#!/usr/bin/env python3
# usage: cat output.log | python3 solve.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from sympy import invert
import gmpy2
gmpy2.get_context().precision = 2048

n = int(input())
ct = eval(input())

p = int(gmpy2.sqrt(n))
while n % p != 0:
    p += 1
q = n // p

assert p * q == n

e = 65537
phi = (p-1)*(q-1)
d = int(invert(e, phi))
key = RSA.construct((n, e, d, p, q))
rsa = PKCS1_OAEP.new(key)
print(rsa.decrypt(ct).decode())
