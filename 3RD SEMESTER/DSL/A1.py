# NUMBER OF STUDENTS IN SECOMP
n = int(input("Enter number of students in SE Computer = "))
list = []
sum = 0
for i in range(0, n):
    name = input("Enter names of each student = ")
    list.append(name)
print("List of total students in SE Computer : ", list)

# NUMBER OF STUDENTS WHO TOOK PART IN CRICKET
n = int(input("Enter number of students who took part in cricket = "))
list1 = []
sum = 0
for i in range(0, n):
    name = input("Enter names of each student (cricket) = ")
    list1.append(name)
print("List of total cricket students: ", list1)

# NUMBER OF STUDENTS WHO TOOK PART IN BADMINTON
n = int(input("Enter number of students who took part in badminton = "))
list2 = []
sum = 0
for i in range(0, n):
    name = input("Enter names of each student (badminton) = ")
    list2.append(name)
print("List of total badminton students : ", list2)

# NUMBER OF STUDENTS WHO TOOK PART IN FOOTBALL
n = int(input("Enter number of students who took part in football = "))
list3 = []
sum = 0
for i in range(0, n):
    name = input("Enter names of each student (football) = ")
    list3.append(name)
print("List of total football students: ", list3)

# Question 1 Function
def Q1(list1, list2):
    list4 = []
    for val in list1:
        if val in list2:
            list4.append(val)
    print("List of students who play both cricket and badminton : ", list4 )

# Question 2 Function
D1 = []
for i in list1:
    if i not in list2:
        D1.append(i)

# badminton-cricket
D2 = []
for i in list2:
    if i not in list1:
        D2.append(i)

def Q2(D1, D2):
    list2 = []
    list2 = D1.copy()
    for val in D2:
        if val not in D1:
            list2.append(val)
    print("List of students who play either cricket or badminton but not both :",  list2)

# Question 3 Function
list5 = []
list5 = list1.copy()
for i in list2:
    if i not in list1:
        list5.append(i)
def Q3():
    list6 = []
    for i in list:
        if i not in list5:
            list6.append(i)
    print("List of students who play neither cricket nor badminton:", list6)


# Question 4 function
list7 = []
for val in list1:
    if val in list3:
        list7.append(val)

def Q4():
    list8 = []
    for i in list7:
        if i not in list2:
            list8.append(i)
    print("Number of students who play cricket and football but not badminton : ", len(list8))

# Menu
while True:
    print("\n\n.........MENU......\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch = int(input("Enter your Choice (from 1 to 5):"))
    if ch == 1:
        Q1(list1,list2)
    elif ch == 2:
        Q2(D1,D2)
    elif ch==3:
        Q3()
    elif ch==4:
        Q4()
    elif ch==5:
        print("Are you sure you want to exit?")
        ans = input("Do you want to contiue? (Y/N)")
        if ans == "Y":
            break
    else:
        print("Wrong Choice!")