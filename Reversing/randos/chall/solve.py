from ctypes import CDLL
from pwn import *
import math
libc = CDLL("libc.so.6")



secret = [0x6c,0x6f,0x6c,0x20,0x69,0x74,0x73,0x20,0x72,0x61,0x6e,0x64]
now = int(math.floor(time.time()-1))
io = remote('io.ept.gg',30050)
#io = process('./randos')

print(now)
libc.srand(now+1)
for i in range(3):
    io.recvuntil(b'>')
    io.sendline('1')
    libc.rand()

io.sendline('1')
io.recvuntil('key: ')
a = libc.rand() & 0xc0de
for i in range(a):
    libc.rand()
for i, j  in enumerate(secret):
    io.sendline(str((j ^ libc.rand()) << i))
io.interactive()
