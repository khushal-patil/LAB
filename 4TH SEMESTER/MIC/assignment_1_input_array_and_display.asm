%macro disp 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .data
	msg1 db "Enter 5 Numbers of Length 64-bit numbers: ",10
	len1 equ $-msg1
	msg2 db "Entered Numbers are: ", 10
	len2 equ $-msg2
	count db 05

section .bss
	array resb 100
section .text
	global _start
_start:
	mov rbx,00
	disp msg1,len1
	
	up:
		mov rax,00
		mov rdi,00
		mov rsi,array
		add rsi,rbx
		mov rdx,17
		syscall
		add rbx,17
		dec byte[count]
		jnz up

	mov byte[count],05
	mov rbx,00
	disp msg2,len2

	up1:
		mov rax,01
		mov rdi,01
		mov rsi,array
		add rsi,rbx
		mov rdx,17
		syscall
		add rbx,17
		dec byte[count]
		jnz up1

	mov rax,60
	mov rdi,00
	syscall