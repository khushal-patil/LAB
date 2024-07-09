%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

%macro read 2
mov rax,0
mov rdi,0
mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .data
	m1 db 10d,13d,"Enter a String: "
	l1 equ $-m1
	m2 db 10d,13d,"Entered a String: "
	l2 equ $-m2
	m3 db 10d,13d,"Length of String: "
	l3 equ $-m3
	
section .bss
	buffer resb 50
	size equ $-buffer
	count resd 1
	dispnum resb 16

section .text
	global _start
	_start:
		print m1,l1
		read buffer,size
		mov [count],rax
		print m2,l2
		print buffer,[count]
		call display
Exit:
		mov ax,60
		mov rbx,0
		syscall
	display:
		mov rsi,dispnum+15
		mov rax,[count]
		mov rcx,16
		dec rax
	UP1:
		mov rdx,0
		mov rbx,10
		div rbx
		add dl,30h
		mov [rsi],dl
		dec rsi
		loop UP1
		print m3,l3
		print dispnum,16
ret
