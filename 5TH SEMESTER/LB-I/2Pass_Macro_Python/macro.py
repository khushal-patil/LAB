file = []
with open("input.txt", "r") as f:
    file = f.readlines()

f = open("mdt.txt", "w")
f.close()
f = open("mdt.txt", "r")
f2 = f.readlines()
f.close()
mdpt = len(f2) + 1

ala = []
mnt = open("mnt.txt", "w")
mdt = open("mdt.txt", "w")
ic = open("ic.txt", "w")
flag = 0

for line in file:
    l = str(line[0:len(line)-1])
    if l == "MACRO":
        flag = 1
    elif l == "MEND":
        mdt.write(l + "\n")
        mdpt += 1
        flag = 0
        
    elif flag == 1:
        mdt.write(l + "\n")
        temp = str(l).split()
        mnt.write(temp[0] + " " + str(mdpt) + "\n")
        ala = str(temp[1]).split(",")
        mdpt += 1
        flag += 1

    elif flag > 1:
        temp = str(l).split()
        part2 = str(temp[1]).split(",")
        mdt.write(temp[0] + " ")
        args = []
        for i in part2:
            substituted = False
            for j in range(len(ala)):
                t = str(ala[j]).split("=")
                if t[0] == i:  
                    args.append("#" + str(j))
                    substituted = True
                    break
            if not substituted:  
                args.append(i)

        mdt.write(",".join(args) + "\n")
        mdpt += 1
    else:
        ic.write(line)
    
ic.close()
mnt.close()
mdt.close()

ic = open("ic.txt", "r")
mnt = open("mnt.txt", "r")
mdt = open("mdt.txt", "r")
i = ic.readlines()
n = mnt.readlines()
m = mdt.readlines()
ic.close()
mnt.close()
mdt.close()

arg_file = open("arg.txt", "w")

f = open("output.txt", "w")
for line in i:
    flag = 0
    temp = str(line).split()

    for i2 in n:
        t = str(i2).split()
        if t[0] == temp[0]:  
            flag = 1
            mdpt = int(str(t[1]))
            break
    
    if flag == 1:
        
        ala = str(temp[1]).split(",")
        flag += 1

        lis = []
        for i2 in range(mdpt - 1, len(m)):
            st = str(m[i2])[0:len(m[i2]) - 1]
            if st == "MEND":
                break
            else:
                lis.append(st)
        
        ala2 = []
        for item in range(len(lis)):
            tmp = str(lis[item]).split()
            if item == 0:
                ala2 = str(tmp[1]).split(",")
                 
                arg_file.write(f"Macro Name: {temp[0]}\n")
                arg_file.write("Formal Parameters: " + ", ".join(ala2) + "\n")
                arg_file.write("Actual Parameters: " + ", ".join(ala) + "\n\n")

            if item > 0:
                f.write(tmp[0] + " ")

            tmp = str(tmp[1]).split(",")
            buffer = ""

            for k in tmp:
                for ii in range(len(ala2)):
                    if k == "#" + str(ii):
                        
                        if ii < len(ala) and ala[ii] != "":
                            buffer += ala[ii] + ","
                        else:
                            buffer += ala2[ii] + ","
            if item > 0:
                f.write(buffer[0:len(buffer) - 1] + "\n")

    elif flag == 0:
        f.write(line)
f.close()
arg_file.close()


