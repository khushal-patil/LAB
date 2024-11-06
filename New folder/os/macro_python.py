MNT={}
MDT=[]
intermediate_code=[]

def pass1(source_code):
	inside_macro=False
	macro_name=""
	
	for line in source_code:
		words=line.strip().split()

		if words[0]=="MACRO":
			inside_macro=True
			continue

		if inside_macro:
			if words[0] not in MNT:
				macro_name=words[0]
				MNT[macro_name]=len(MDT)
			MDT.append(" ".join(words))
			if words[0] =="MEND":
				inside_macro=False
				continue

		intermediate_code.append(line)

def pass2(intermediate_code):
	output_code=[]

	for line in intermediate_code:
		words=line.strip().split()
		
		if words[0] in MNT:
			macro_start=MNT[words[0]]
			
			for i in range(macro_start,len(MDT)):
				if MDT[i]=="MEND":
					break
				output_code.append(MDT[i])
		else:
			output_code.append(line)

	return output_code

source_code=[
	"MACRO",
	"INCR &ARG",
	"LDA &ARG",
	"ADD =1",
	"STA &ARG",
	"MEND",
	"START",
	"INCR X",
	"INCR y",
	"END"
]	

pass1(source_code)

print("\nMNT:",MNT)
print("\nMDT:",MDT)
print("\nintermediate code:",intermediate_code)

final_code=pass2(intermediate_code)

print("\nfinal output code after pass2:")

for line in final_code:
	print(line)
		