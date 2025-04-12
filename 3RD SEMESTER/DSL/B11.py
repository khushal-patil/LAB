def linear_search(roll_numbers, target):
    for roll_number in roll_numbers:
        if roll_number == target:
            return True
    return False 

def sentinel_search(arr, n, key):
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0
    while (arr[i] != key):
        i=i+1
    arr[n - 1] = last
    if ((i < n - 1) or (arr[n - 1] == key)):
        print(f"\nElement { key} found.")
    else:
        print("\nElement not found.")

def binary_search(roll_numbers, target):
    left, right = 0, len(roll_numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if roll_numbers[mid] == target:
            return True
        elif roll_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def fibonacci_search(roll_numbers, target):
    def generate_fibonacci_sequence(n):
        fibonacci = [0, 1]
        while fibonacci[-1] < n:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci

    n = len(roll_numbers)
    fibonacci = generate_fibonacci_sequence(n)

    offset = -1

    while fibonacci:
        i = min(offset + fibonacci[-2], n - 1)
        if roll_numbers[i] == target:
            return True
        elif roll_numbers[i] < target:
            fibonacci = fibonacci[:-2]
            offset = i
        else:
            fibonacci = fibonacci[:-1]
    return False

while True:
    print("\n********** Welcome to Searching **************")
    print("1. Unsorted List")
    print("2. Sorted List")
    print("3. Exit")
    ch = int(input("Enter Choice: "))
    if ch==1:
        while True:
            print("1. Linear Search")
            print("2. Sentinel Search")
            print("3. Exit")
            ch = int(input("Enter Choice: "))
            if ch==1:
                roll_no=[]
                n = int(input("Enter No of Students: "))
                for i in range(n):
                    s = int(input(f"Enter {i+1} Student Roll No: "))
                    roll_no.append(s)
                search = int(input("\n Enter Roll No You want to Search: "))
                if linear_search(roll_no,search)==True:
                    print(f"\nElement { search} found.")
                else:
                    print("\nElement no found.")

            elif ch==2:
                roll_no=[]
                n = int(input("Enter No of Students: "))
                for i in range(n):
                    s = int(input(f"Enter {i+1} Student Roll No: "))
                    roll_no.append(s)
                search = int(input("\n Enter Roll No You want to Search: "))
                sentinel_search(roll_no,n,search)
            elif ch==3:
                break
            else:
                print("Invalid Choice...")
    elif ch==2:
        while True:
            print("1. Binary Search)")
            print("2. Fibonacci Search")
            print("3. Exit")
            ch = int(input("Enter Choice: "))
            if ch==1:
                roll_no=[]
                n = int(input("Enter No of Students: "))
                for i in range(n):
                    s = int(input(f"Enter {i+1} Student Roll No: "))
                    roll_no.append(s)
                search = int(input("\n Enter Roll No You want to Search: "))
                if binary_search(roll_no,search)==True:
                    print(f"\nElement { search} found.")
                else:
                    print("\nElement no found.")
            elif ch==2:
                roll_no=[]
                n = int(input("Enter No of Students: "))
                for i in range(n):
                    s = int(input(f"Enter {i+1} Student Roll No: "))
                    roll_no.append(s)
                search = int(input("\n Enter Roll No You want to Search: "))
                if fibonacci_search(roll_no,search)==True:
                    print(f"\nElement { search} found.")
                else:
                    print("\nElement no found.")
            elif ch==3:
                break
            else:
                print("Invalid Choice...")
    elif ch==3:
        print("Thank You")
        break
    else:
        print("Invalid Choice...")