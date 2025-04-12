
stud=[]
def accept():
    n = int(input("Enter Total Number of Students : "))
    for i in range(n):
        val = float(input("Enter Percentage : "))
        stud.append(val)

def display():
    print("\nStudents List : ", stud)

def selection():
    n = len(stud)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if stud[j] < stud[min_index ]:
                min_index = j
        stud[i], stud[min_index] = stud[min_index], stud[i]

    print(stud)

def bubble():
    n = len(stud)
    for i in range(n):
        for j in range(0, n-i-1):
            if stud[j] > stud[j+1]:
                stud[j], stud[j+1] = stud[j+1], stud[j]
    print(stud)

while(True):
    print("\n1. Enter Student Percentage")
    print("2. Display")
    print("3. Selection Sort")
    print("4. Bubble Sort")
    print("5. Exit")
    ch = int(input("Enter Choice : "))

    if ch==1:
        accept()
    elif ch==2:
        display()
    elif ch==3:
        selection()
    elif ch==4:
        bubble()
    elif ch==5:
        break
    else:
        print("Invalid Choice...")