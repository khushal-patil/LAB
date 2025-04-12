string = input("Enter a String : ")

# To display word with the longest length
def Q1():
    string2 = string.split(" ")
    lenw =[]
    for i in string2:
        lenw.append(len(i))
    index = lenw.index(max(lenw))
    print("The word with the longest length :",string2[index])

# to determine the frequency of a particular character
def Q2():
    n = input("Enter character which you want to find:")
    occurenced = 0
    for i in string:
        if i == n:
            occurenced = occurenced + 1
    print("The letter '",n, "'is occured ", occurenced, " times")

 # To check whether given string in palindrome or not
def Q3():
    str1 = ""
    for i in string:
        str1 = i + str1
    if str1 == string:
        print("The string is palindrome")
    else:
        print("The string is not a palindrome ")

# To diplay index of first appearance of the sub string
def Q4():
    n = input("Enter a substring : ")
    count = 0
    for i in range(0,len(string)):
        match = True
        if n[0] == string[i]:
            j = 0
            for j in range(0,len(n)):
                if n[j]!=string[i+j]:
                    match = False
                    break
                else:
                    count=count+1
                if match == True and count == len(n):
                    print("substring found at position : ",i)

# To count the occurrences of each word in a given string
def Q5():
    words = string.split()
    unique_words = []
    word_counts = []

    for word in words:
        word = word.lower()
        if word in unique_words:
            index = unique_words.index(word)
            word_counts[index] += 1
        else:
            unique_words.append(word)
            word_counts.append(1)

    for i in range(len(unique_words)):
        print(f"'{unique_words[i]}' occurs {word_counts[i]} times.")


# to copy the given string
def Q6():     
    str2 = string
    print("The copy of the given string is : ", str2)

# Menu
while True:
    print("\n.........MENU......\n")
    print("1. To display word with the longest length")
    print("2. To determines the frequency of occurrence of particular character in the string")
    print("3. To check whether given string in palindrome or not")
    print("4. To diplay index of first appearance of the substring")
    print("5. To count the occurrences of each word in a given string")
    print("6. To Copy String")
    print("7. Exit\n")
    ch = int(input("Enter your Choice (from 1 to 7):"))
    if ch == 1:
        Q1()
    elif ch == 2:
        Q2()
    elif ch==3:
        Q3() 
    elif ch==4:
        Q4()
    elif ch==5:
        Q5()
    elif ch==6:
        Q6()
    elif ch==7:
        print("Thank You...")
        break
    else:
        print("Wrong Choice!")