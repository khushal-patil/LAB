str = "Hello "
cmp = "aeiou"
vcount=0
count=0
for i in str:
    if i in cmp:
        vcount+=1
    elif i == " ":
        pass
    else:
        count+=1
        
        
print(vcount)
print(count)