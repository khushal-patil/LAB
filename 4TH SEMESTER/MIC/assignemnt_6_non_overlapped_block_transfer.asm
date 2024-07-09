; program to do non-overlapped block data transfer

%macro print 2
mov rax,1
mov rdi,1

mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .data
msg db 10, 'block contents before transfer',10,13
msglen equ $-msg

msg2 db 10,13, 'block contents after transfer',10,13
msg2len equ $-msg2

msg3 db 10,13,'SRC Block :- '
msg3len equ $-msg3

msg4 db 10,13,'DEST Block:- '
msg4len equ $-msg4

space db ' '
srcblk db 10h,20h,30h,40h,50h
destblk db 0,0,0,0,0
cnt equ 5

section .bss
ans resb 4
section .text
global _start
_start:
    print msg,msglen
    print msg3,msg3len
    mov rsi,srcblk
    call disp_block
    
    print msg4,msg4len
    mov rsi,destblk
    call disp_block
    
    mov rcx,05h
    mov rsi,srcblk
    mov rdi,destblk
    
s1:
    mov al,[rsi]
    mov [rdi],al
    inc rsi
    inc rdi
    loop s1
    
    print msg2,msg2len
    print msg3,msg3len
    mov rsi,srcblk
    call disp_block
    
    print msg4,msg4len
    mov rsi,destblk
    call disp_block
    
    mov rax,60
    syscall
    
disp_block:
    mov rbp,cnt
    
back:
    mov al,[rsi]
    mov bl,al
    push rsi
    call disp_8
    print space,1
    pop rsi
    inc rsi
    dec rbp
    jnz back
    ret

disp_8:
    mov rsi,ans
    mov rcx,02
    dispup1:
        rol bl,4
        mov dl,bl
        and dl,0fh
        add dl,30h
        cmp cl,39h
        jbe dispskip1
        add dl,07h
    dispskip1:
        mov [rsi],dl
        inc rsi
        loop dispup1
        print ans,2
    ret