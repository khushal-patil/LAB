def Q1(marks):
    if not marks:
        return 0
    total = 0
    count = 0
    for mark in marks:
        total += mark
        count += 1

    average = total / count
    return average

def Q2(marks):
    if not marks:
        return None, None
    highest = marks[0]
    lowest = marks[0]
    
    for mark in marks:
        if mark > highest:
            highest = mark
        elif mark < lowest and mark !=0:
            lowest = mark
    return highest, lowest


def Q3(marks):
    count=0
    for i in marks:
        if i ==0:
            count+=1
    return count

def Q4(marks):
    if not marks:
        return None
    mark_count = {}
    for mark in marks:
        if mark in mark_count:
            mark_count[mark] += 1
        else:
            mark_count[mark] = 1
    mcm = max(mark_count, key=mark_count.get)
    return mcm

n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
        mark = float(input(f"Enter the marks of student {i+1}: "))
        marks.append(mark)
        
while True:
    print("\n*********Menu***********")
    print("1. Calculate average score of the class")
    print("2. Find the highest and lowest scores in the class")
    print("3. Count of students absent for the test")
    print("4. Display mark with the highest frequency")
    print("5. Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == '1':
        average = Q1(marks)
        print(f"Average score of the class: {average}")
    elif choice == '2':
        highest, lowest = Q2(marks)
        print(f"Highest score in the class: {highest}")
        print(f"Lowest score in the class: {lowest}")
    elif choice == '3':
        absent_students = Q3(marks)
        print(f"Count of students absent for the test: {absent_students}")
    elif choice == '4':
        mcm = Q4(marks)
        print(f"Mark with the highest frequency: {mcm}")
    elif choice == '5':
        print("Thank You...")
        break
    else:
        print("Invalid choice")
