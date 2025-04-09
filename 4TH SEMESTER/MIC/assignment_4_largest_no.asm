%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

section .data
    m1 db 10,13,"Largest Number from Array is: "
    l1 equ $-m1
    
    array db 01h,33h,0Fh,11h,45h
    large db 00h
    
    m2 db "",10,13
    l2 equ $-m2
    
section .bss
    dispnum resb 2

section .text
    global _start
    _start:
        print m1,l1
        
        mov bl,0FFh
        
        mov rsi,array
        mov rcx,05
        
    back:
        cmp [rsi],bl
        jl skip
        mov bl,[rsi]
    skip:
        add rsi,1
        loop back
            
        mov byte[large],bl
        call display
Exit:
        mov rax,60
        mov rbx,0
        syscall
        
display:
            mov rdi,dispnum
            mov bl,byte[large]
            mov rcx,2
dispup1:
            rol bl,4
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
                print dispnum,2
                print m2,l2
ret
    
 