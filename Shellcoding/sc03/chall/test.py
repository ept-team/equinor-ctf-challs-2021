from pwn import *
context.arch = 'amd64'
for i in range(255):
    print(disasm(bytes([i])))