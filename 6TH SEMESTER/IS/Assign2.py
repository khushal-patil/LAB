import math
def encryptMessage(msg):
    cipher = ""
    k_indx = 0
    msg = msg.replace(" ", "#")
    msg_len = len(msg)
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    
    for i in range(col):
        curr_idx = key_order[i]
        cipher += ''.join([row[curr_idx] for row in matrix])
    return cipher

def decryptMessage(cipher):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = len(cipher)
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    
    for _ in range(row):
        dec_cipher += [[None] * col]
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    
    for k in range(col):
        curr_idx = key_order[k]
        
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
    msg = ''.join(sum(dec_cipher, []))
    msg = msg.replace("_", "") 
    msg = msg.replace("#", " ")  
    return msg


msg = input("Enter the Plain Text: ")
key = input("Enter the Key: ")
cipher = encryptMessage(msg)
print("Encrypted Message:", cipher)

print("Decrypted Message:", decryptMessage(cipher))

