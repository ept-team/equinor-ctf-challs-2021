#!/usr/bin/env python3
import binascii
from pwn import *

context.arch = 'amd64'

shellcode = shellcraft.pushstr("Provide input:\n")
shellcode += """
            push rsp
            pop rsi

            /* write: */
            mov rax,1
            mov rdi,1
            mov rdx,15
            syscall
"""

shellcode += """

        /* read: */
        mov rax, 0
        mov rdi, 0
        sub rsp, 1
        mov rsi, rsp
        mov rdx, 1
        syscall

        mov dil, byte ptr[rsp]
        lea rax,[rip]
        add rax,rdi
        jmp rax
"""

shellcode += """
            lea rdi, qword ptr [rip+12]

            decrypt:
            xor byte ptr [rdi],0x90
            mov al, byte ptr [rdi]
            inc rdi
            cmp al,0x90 
            jnz decrypt
"""
# shellcode += "tmp:\n"
# shellcode += shellcraft.pushstr("It is not a correct flag, unfortunately :(\n")
# shellcode += """
#         push rsp
#         pop r13
#         """
# shellcode += shellcraft.pushstr("Wow, you entered the right flag, impressive!\n")
# shellcode += """
#         push rsp
#         pop r14
#         """

# shellcode += shellcraft.pushstr("\x45\x51\x56\x78\x77\x36\x6a\x61\x57\x64\x3a\x6f\x65\x6b\x77\x3e\x7e\x76\x4d\x70\x24\x71\x73\x48\x29\x6a\x45\x7d\x69\x73\x63")
# shellcode += """
#         push rsp
#         pop r12
# """

# shellcode += shellcraft.pushstr("Input flag for verification:\n")
# shellcode += """
#         push rsp
#         pop rsi

# /* write: */
#         mov rax, 1
#         mov rdi, 1
#         mov rdx, 29
#         syscall

# /* read: */
#         mov rax, 0
#         mov rdi, 0
#         sub rsp, 31
#         mov rsi, rsp
#         mov rdx, 31
#         syscall   

#         mov rcx, 0
#         mov rsi, 0

# loop:
#         mov       dl, [rsp+rcx]
#         xor       rdx, rcx
#         mov       dil, [r12+rcx]
#         xor       dl, dil
#         add       rsi,rdx
#         inc       rcx
#         cmp       rcx, 31
#         jne       loop
#         test      rsi,rsi
#         jnz       bad

# good:
#         mov       rax, 1
#         mov       rdi, 1
#         mov       rsi, r14
#         mov       rdx, 45
#         syscall
#         jmp       exit

# bad:
#         mov       rax, 1
#         mov       rdi, 1
#         mov       rsi, r13
#         mov       rdx, 43
#         syscall

# exit:
#         mov       rax, 60
#         xor       rdi, rdi
#         syscall

#         nop

# """

binaryCode = asm(shellcode)

print(binascii.hexlify(binaryCode))
# EPT{s3lf_m0dify1ng_c0de_1s_fun}

# banner:    db "Input flag for verification:", 10
# wrong:     db "It is not a correct flag, unfortunately :(", 10
# correct:   db "Wow, you entered the right flag, impressive!", 10
# temp:      db 0x45,0x51,0x56,0x78,0x77,0x36,0x6a,0x61,0x57,0x64,0x3a,0x6f,0x65,0x6b,0x77,0x3e,0x7e,0x76,0x4d,0x70,0x24,0x71,0x73,0x48,0x29,0x6a,0x45,0x7d,0x69,0x73,0x63
# buffer:    resb 31
# output:    resb 31

        # mov       rcx, 0
        # mov       rsi, 0
# loop:

#           mov       dl, [buffer+rcx]
#           xor       rdx, rcx
#           mov       dil, [temp+rcx]
#           xor       dl, dil
#           add       rsi,rdx
#           inc       rcx
#           cmp       rcx, 31
#           jne       loop
#           test      rsi,rsi
#           jnz       bad

# good:
#           mov       rax, 1
#           mov       rdi, 1
#           mov       rsi, correct
#           mov       rdx, 45
#           syscall
#           jmp       exit

# bad:
#           mov       rax, 1
#           mov       rdi, 1
#           mov       rsi, wrong
#           mov       rdx, 43
#           syscall

# exit:
#           mov       rax, 60
#           xor       rdi, rdi
#           syscall
                        