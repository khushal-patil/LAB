

SetA = [] 
SetB = []

def insert():
	n1 = int(input("Enter the number of elements in Set A: "))
	for i in range(n1):
		nm = int(input("Enter the element in Set A: "))
		SetA.append(nm)
		
	n1 = int(input("Enter the number of elements in Set B: "))
	for i in range(n1):
		nm = int(input("Enter the element in Set B: "))
		SetB.append(nm)
		
def display():
	print("Set A : ",SetA)
	print("Set B : ",SetB)
	
	
def union():
	res=[]
	for i in SetA:
		res.append(i)
	for i in SetB:
		if i not in res:
			res.append(i)
	
	print("Union: ",res)

def intersection():
	res =[]
	for i in SetA:
		if i in SetB:
			res.append(i)
			
	print("Intersection: ",res)

def difference():
	res =[]
										
	for i in SetA:
		if i not in SetB:
			res.append(i)
			
	for i in SetB:
		if i not in SetA:
			res.append(i)
	print("Difference: ",res)
	
	
def find():
	t = int(input("1. Set A or 2. Set B: "))
	s=False
	s = int(input("Enter Element to Search: "))
	if t==1:
		for i in range(len(SetA)):
			if s == SetA[i]:
				s = True
		if s == True:
			print("Element Found...")
		else:
			print("Element Not Found...")
	elif t==2:
		for i in range(len(SetB)):
			if s == SetB[i]:
				s = True
		if s == True:
			print("Element Found...")
		else:
			print("Element Not Found...")

def remove():
	t = int(input("1. Set A or 2. Set B: "))
	s=False
	s1 = int(input("Enter Element to Deleted: "))
	if t==1:
		for i in range(len(SetA)):
			if s1 == SetA[i]:
				s = True
		if s == True:
			print("Element Found...")
			SetA.remove(s1)
			print("After Deletion",SetA)
		else:
			print("Element not in Set A.")
	elif t==2:
		for i in range(len(SetB)):
			if s1 == SetB[i]:
				s = True
		if s == True:
			print("Element Found...")
			SetB.remove(s1)
			print("After Deletion",SetB)
		else:
			print("Element not in Set B.")
		
def size():
	ct=0
	for i in SetA:
		ct+=1  
	print("Size of SetA: ",ct)
	ct=0
	for i in SetB:
		ct+=1
	print("Size of SetB: ",ct)
							 
def subset():
	set5 = []
	flag=False
	for i in SetA:
		if i in SetB:
			set5.append(i)
			flag=True
		
	if flag==True:
		print("Subset",set5)
		print("SetB is a Subset of SetA.")
	else:
		print("SetB is not Subset of SetA.")
	
while True:
	print("******* Set Operations ******")
	print("1. Insert")
	print("2. Display")
	print("3. Union ")
	print("4. Intersection")
	print("5. Difference")
	print("6. Size of Sets")
	print("7. Find ")
	print("8. Delete an Element")
	print("9. Subset")
	print("0. Exit")
	
	ch = int(input("Enter the Choice: "))
	
	if ch==1:
		insert()
	elif ch==2:
		display()
	elif ch==3:
		union()
	elif ch==4:
		intersection()
	elif ch==5:
		difference()
	elif ch==6:
		size()
	elif ch==7:
		find()
	elif ch==8:
		remove()
	elif ch==9:
		subset()
	elif ch==0:
		break
	else:
		print("Invalid Choice...")


