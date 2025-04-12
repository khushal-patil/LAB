
perc = []
number_of_students = int(input("Enter the number of Students : "))
for i in range(number_of_students):
    perc.append(float(input("Enter the percentage of Student {0} : ".format(i+1))))


# Function for performing partition of the Data
def percentage_partition(perc,start,end):
    pivot = perc[start]
    i = start + 1
    j = end

    while True:
        while i <= j and perc[i] <= pivot:
            i += 1
            
        while i <= j and perc[j] >= pivot:
            j -= 1
        if i <= j:
            perc[i],perc[j] = perc[j],perc[i]
        else:
            break
    perc[start],perc[j] = perc[j],perc[start]
    return j

# Function for performing Quick Sort on the Data
def Quick_Sort(perc,start,end):
    while start < end:
        partition = percentage_partition(perc,start,end)
        Quick_Sort(perc,start,partition-1)
        Quick_Sort(perc,partition+1,end)
        return perc


# Function for Displaying Top Five Percentages of Students
def display_top_five(perc):
    print("Top Five Percentages are : ")
    if len(perc) < 5:
        start, stop = len(perc) - 1, -1
    else:
        start, stop = len(perc) - 1, len(perc) - 6

    for i in range(start, stop, -1):
        print(perc[i],sep = "\n") 

# Main
sorted_percentage = []
while True:
    print("\n--------------------MENU--------------------")
    print("1. Display the Percentages of Students")
    print("2. Perform Quick Sort on the Data")
    print("3. Exit")
    ch = int(input("Enter your choice (from 1 to 3) : "))

    if ch == 1:
        print("Percentage : ",perc)

    elif ch == 2:
        print("Percentages of Students after performing Quick Sort : ")
        sorted_percentage = Quick_Sort(perc,0,len(perc)-1)
        print(sorted_percentage)
        ans = input("Are you want to Display Top 5 Percentage(Y/N)")
        if ans == "Y":
            display_top_five(sorted_percentage)
        
    elif ch == 3:
        print("Thank You.")
        break
    else:
        print("Wrong Choice!!")