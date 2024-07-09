section .data
	msg db 10,13,"Welcome to sppu MPL Lab",10
	msglen equ $-msg
section .bss
section .text
	global _start
	_start:
;display
	MOV Rax, 1
	MOV Rdi, 1
	MOV rsi, msg
	MOV Rdx, msglen
	syscall
;exit sys call
	MOV Rax, 60
	MOV Rdi, 0
	syscall
