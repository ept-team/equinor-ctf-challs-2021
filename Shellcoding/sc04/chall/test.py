from pwn import *
context.arch = 'amd64'
shellcode = """
    push rsp;
    pop rsi;
    mov [rsi], r15;
    add rsi, 8;
    mov [rsi], r15;
"""

ELF.from_assembly(shellcode).debug().interactive()