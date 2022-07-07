	.file	"bofish.c"
	.intel_syntax noprefix
	.text
	.globl	ignore_me_init_buffering
	.type	ignore_me_init_buffering, @function
ignore_me_init_buffering:
.LFB6:
	.cfi_startproc
	endbr64
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	mov	rax, QWORD PTR stdout[rip]
	mov	ecx, 0
	mov	edx, 2
	mov	esi, 0
	mov	rdi, rax
	call	setvbuf@PLT
	mov	rax, QWORD PTR stdin[rip]
	mov	ecx, 0
	mov	edx, 2
	mov	esi, 0
	mov	rdi, rax
	call	setvbuf@PLT
	mov	rax, QWORD PTR stderr[rip]
	mov	ecx, 0
	mov	edx, 2
	mov	esi, 0
	mov	rdi, rax
	call	setvbuf@PLT
	nop
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	ignore_me_init_buffering, .-ignore_me_init_buffering
	.section	.rodata
	.align 8
.LC0:
	.string	"[!] Anti DoS Signal. Patch me out for testing."
	.text
	.globl	kill_on_timeout
	.type	kill_on_timeout, @function
kill_on_timeout:
.LFB7:
	.cfi_startproc
	endbr64
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 16
	mov	DWORD PTR -4[rbp], edi
	cmp	DWORD PTR -4[rbp], 14
	jne	.L4
	lea	rdi, .LC0[rip]
	mov	eax, 0
	call	printf@PLT
	mov	edi, 0
	call	_exit@PLT
.L4:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	kill_on_timeout, .-kill_on_timeout
	.section	.rodata
	.align 8
.LC1:
	.string	" _______   __       __  __    __    __    ______  "
	.align 8
.LC2:
	.string	"|       \\ |  \\  _  |  \\|  \\  |  \\ _/  \\  /      \\ "
	.align 8
.LC3:
	.string	"| $$$$$$$\\| $$ / \\ | $$| $$\\ | $$|   $$ |  $$$$$$\\"
	.align 8
.LC4:
	.string	"| $$__/ $$| $$/  $\\| $$| $$$\\| $$ \\$$$$  \\$$__| $$"
	.align 8
.LC5:
	.string	"| $$    $$| $$  $$$\\ $$| $$$$\\ $$  | $$   |     $$"
	.align 8
.LC6:
	.string	"| $$$$$$$ | $$ $$\\$$\\$$| $$\\$$ $$  | $$  __\\$$$$$\\"
	.align 8
.LC7:
	.string	"| $$      | $$$$  \\$$$$| $$ \\$$$$ _| $$_|  \\__| $$"
	.align 8
.LC8:
	.string	"| $$      | $$$    \\$$$| $$  \\$$$|   $$ \\$$    $$"
	.align 8
.LC9:
	.string	" \\$$       \\$$      \\$$ \\$$   \\$$ \\$$$$$$ \\$$$$$$ "
	.align 8
.LC10:
	.string	"\n Welcome to PWN13, the awesome encryption engine!"
	.align 8
.LC11:
	.string	"At this stage we dont accept strings longer than 100 characters, so play nice :)"
	.text
	.globl	banner
	.type	banner, @function
banner:
.LFB8:
	.cfi_startproc
	endbr64
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	lea	rdi, .LC1[rip]
	call	puts@PLT
	lea	rdi, .LC2[rip]
	call	puts@PLT
	lea	rdi, .LC3[rip]
	call	puts@PLT
	lea	rdi, .LC4[rip]
	call	puts@PLT
	lea	rdi, .LC5[rip]
	call	puts@PLT
	lea	rdi, .LC6[rip]
	call	puts@PLT
	lea	rdi, .LC7[rip]
	call	puts@PLT
	lea	rdi, .LC8[rip]
	call	puts@PLT
	lea	rdi, .LC9[rip]
	call	puts@PLT
	lea	rdi, .LC10[rip]
	call	puts@PLT
	lea	rdi, .LC11[rip]
	call	puts@PLT
	nop
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE8:
	.size	banner, .-banner
	.globl	ignore_me_init_signal
	.type	ignore_me_init_signal, @function
ignore_me_init_signal:
.LFB9:
	.cfi_startproc
	endbr64
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	lea	rsi, kill_on_timeout[rip]
	mov	edi, 14
	call	signal@PLT
	mov	edi, 60
	call	alarm@PLT
	nop
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE9:
	.size	ignore_me_init_signal, .-ignore_me_init_signal
	.globl	rot13
	.type	rot13, @function
rot13:
.LFB10:
	.cfi_startproc
	endbr64
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	mov	QWORD PTR -24[rbp], rdi
	mov	DWORD PTR -4[rbp], 0
	mov	DWORD PTR -4[rbp], 0
	jmp	.L8
.L15:
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 96
	jle	.L9
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 109
	jle	.L10
.L9:
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 96
	jle	.L11
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 109
	jg	.L11
.L10:
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	lea	ecx, 13[rax]
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	mov	edx, ecx
	mov	BYTE PTR [rax], dl
	jmp	.L12
.L11:
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 109
	jle	.L13
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 122
	jle	.L14
.L13:
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 77
	jle	.L12
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	cmp	al, 90
	jg	.L12
.L14:
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	lea	ecx, -13[rax]
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	mov	edx, ecx
	mov	BYTE PTR [rax], dl
.L12:
	add	DWORD PTR -4[rbp], 1
.L8:
	mov	eax, DWORD PTR -4[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -24[rbp]
	add	rax, rdx
	movzx	eax, BYTE PTR [rax]
	test	al, al
	jne	.L15
	nop
	nop
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE10:
	.size	rot13, .-rot13
	.section	.rodata
.LC12:
	.string	"Enter text: "
.LC13:
	.string	"Result: "
	.text
	.globl	main
	.type	main, @function
main:
.LFB11:
	.cfi_startproc
	endbr64
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	add	rsp, -128
	mov	rax, QWORD PTR fs:40
	mov	QWORD PTR -8[rbp], rax
	xor	eax, eax
	mov	DWORD PTR -16[rbp], 0
	mov	eax, 0
	call	ignore_me_init_buffering
	mov	eax, 0
	call	ignore_me_init_signal
	mov	eax, 0
	call	banner
	lea	rdi, .LC12[rip]
	mov	eax, 0
	call	printf@PLT
	jmp	.L17
.L20:
	mov	rax, QWORD PTR stdin[rip]
	mov	rdi, rax
	call	fgetc@PLT
	mov	BYTE PTR -117[rbp], al
	cmp	BYTE PTR -117[rbp], 10
	je	.L23
	mov	eax, DWORD PTR -16[rbp]
	cdqe
	movzx	edx, BYTE PTR -117[rbp]
	mov	BYTE PTR -116[rbp+rax], dl
	add	DWORD PTR -16[rbp], 1
.L17:
	mov	rax, QWORD PTR stdin[rip]
	mov	rdi, rax
	call	feof@PLT
	test	eax, eax
	je	.L20
	jmp	.L19
.L23:
	nop
.L19:
	lea	rax, -116[rbp]
	mov	rdi, rax
	call	rot13
	lea	rdi, .LC13[rip]
	mov	eax, 0
	call	printf@PLT
	lea	rax, -116[rbp]
	mov	rdi, rax
	call	puts@PLT
	mov	eax, 0
	mov	rcx, QWORD PTR -8[rbp]
	xor	rcx, QWORD PTR fs:40
	je	.L22
	call	__stack_chk_fail@PLT
.L22:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE11:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
