class Bank:
    def __init__(self):
        self.accno = ""
        self.name = ""
        self.ifsc = ""
        self.Aadhar = ""
        self.previousTransaction = 0.0
        self.balance = 0.0
        self.mobile = 0
        self.next = None

    def show_account(self):
        print("\n\t********** Customer Details **********")
        print("Name: " + self.name)
        print("Account No.: " + self.accno)
        print("IFSC Code: " + self.ifsc)
        print("Aadhar No.: " + self.Aadhar)
        print("Mobile No.: " + str(self.mobile))
        print("Account Balance: Rs. {:.2f}\n".format(self.balance))

    def deposit(self):
        amt = float(input("Enter Amount You Want to Deposit : "))
        self.balance += amt
        self.previousTransaction = amt
        print("Money Deposit Successfully...")
        print("Current Balance: Rs. {:.2f}".format(self.balance))

    def withdraw(self):
        amt = float(input("Enter Amount You Want to withdraw : "))
        if self.balance >= amt:
            self.balance -= amt
            self.previousTransaction = -amt
            print("Money withdraw Successfully...")
            print("Current Balance: Rs. {:.2f}".format(self.balance))
        else:
            print("Insufficient Balance..Transaction Failed..")

    def view_balance(self):
        print("\n\t********** View Balance **********")
        print("Current Balance: Rs. {:.2f}".format(self.balance))

    def get_previous_transaction(self):
        if self.previousTransaction > 0:
            print("Deposited: Rs. {:.2f}".format(self.previousTransaction))
        elif self.previousTransaction < 0:
            print("Withdrawn: Rs. {:.2f}".format(abs(self.previousTransaction)))
        else:
            print("No Transaction occurred")


class LinkedList:
    def __init__(self):
        self.head = None

    def add_customer(self, customer):
        if not self.head:
            self.head = customer
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = customer

    def search_customer(self, acn):
        current = self.head
        while current:
            if current.accno == acn:
                return current
            current = current.next
        return None

print("\t************** Welcome to Miniproject ************** ")
n = int(input("How Many Account You Want to Create : "))
if n != 0:
    bank = LinkedList()
    for _ in range(n):
        customer = Bank()
        print("Enter Your Name: ",end="")
        customer.name = input()
        print("Enter Account No: ",end="")
        customer.accno = input()
        print("Enter IFSC Code: ",end="")
        customer.ifsc = input()
        print("Enter Aadhar No: ",end="")
        customer.Aadhar = input()
        print("Enter Mobile No: ",end="")
        customer.mobile = int(input())
        print("Enter Opening Balance: ",end="")
        customer.balance = float(input())
        bank.add_customer(customer)
        print("\n\t************* Account Created Successfully... ***********")

    ch = 0
    while ch != 7:
        print("\n\t=============== Main Menu ===============")
        print("1. Customer Details")
        print("2. Search By Account No.")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View Balance")
        print("6. Previous Transaction ")
        print("7. Exit")
        ch = int(input("Your Choice: "))

        if ch == 1:

            current = bank.head
            while current:
                current.show_account()
                current = current.next
        elif ch == 2:
            acn = input("Enter Account No. You Want to Search...: ")
            customer = bank.search_customer(acn)
            if customer:
                customer.show_account()
            else:
                print("Search Failed..Account Not Exist..")

        elif ch == 3:
            acn = input("Enter Account No. : ")
            customer = bank.search_customer(acn)
            if customer:
                customer.deposit()
            else:
                    print("Search Failed..Account Not Exist..")
        elif ch == 4:
            acn = input("Enter Account No : ")
            customer = bank.search_customer(acn)
            if customer:
                customer.withdraw()
            else:
                print("Search Failed..Account Not Exist..")
        elif ch == 5:
            acn = input("Enter Account No : ")
            customer = bank.search_customer(acn)
            if customer:
                customer.view_balance()
            else:
                print("Search Failed..Account Not Exist..")
        elif ch == 6:
            acn = input("Enter Account No : ")
            customer = bank.search_customer(acn)
            if customer:
                print("\n")
                customer.get_previous_transaction()
            else:
                print("Search Failed..Account Not Exist..")
        elif ch == 7:
            print("Thank You..")
        else:
            print("Invalid Choice....")