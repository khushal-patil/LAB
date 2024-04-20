section .data
    nummsg db "***Program to find Factorial of a number*** ",10
           db "Enter the number : ",
    nummsg_len equ $-nummsg

    resmsg db "Factorial of entered number is : "
    resmsg_len equ $-resmsg

    zerofact db "0001 "
    zerofactlen equ $-zerofact
    newline db 10 
    
section .bss
    dispbuff resb 6
    result resb 4
    num resb 1
    num1 resb 1
    numascii resb 3

    %macro print 2
       mov rax,01
       mov rdi,01
       mov rsi,%1
       mov rdx,%2
       syscall
    %endmacro

    %macro accept 2
      mov rax,0
      mov rdi,0
      mov rsi,%1
      mov rdx,%2
      syscall
    %endmacro    

section .text
global _start
_start:
  
    print nummsg,nummsg_len
    accept numascii,3            
    call packnum           
    mov [num],bl
    print resmsg,resmsg_len

    mov al,[num]          
    cmp al,01h          
    jbe endfact

    mov bl,[num]
    call proc_fact
    mov rbx,rax
    call disp64_proc
    jmp exit
  
endfact:
    print zerofact,zerofactlen
  
exit:    

    mov rax,60
    mov rdi,0
    syscall
    ret

disp64_proc:
    mov rdi,dispbuff   
    mov rcx,04      
dispup1:
    rol bx,4       
    mov dl,bl       
    and dl,0fh       
    add dl,30h       
    cmp dl,39h        
    jbe dispskip1       
    add dl,07h       

dispskip1:
    mov [rdi],dl        
    inc rdi            
    loop dispup1        
    print dispbuff,05   
    print newline,1 ;
  
    ret

packnum:
    mov bx,0
    mov rcx,02
    mov rsi,numascii
up1:
    rol bl,04
    mov al,[rsi]
    cmp al,39h
    jbe skip1
    sub al,07h
skip1:    sub al,30h
    add bl,al
    inc rsi
    loop up1
    ret

proc_fact:
    cmp bl, 1
    jne calculate_facto
    mov ax, 1
    ret

  calculate_facto:
    push rbx  
    dec bl
    mov ax, 1
  call proc_fact
    pop rbx
    mul bl
    ret







