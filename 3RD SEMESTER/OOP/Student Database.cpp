#include <iostream>
#include <string>

using namespace std;

class College
{
private:
    int roll_no;
    string cls;
    string division;

public:
    static int strength;
    friend class Student;

    College()
    {
        roll_no = 0;
        cls = "";
        division = "";
    }

    void display()
    {
        cout << "Roll no:" << roll_no << endl;
        cout << "Class :" << cls << endl;
        cout << "Division:" << division << endl;
    }

    static void increment()
    {
        strength += 1;
    }

    static void decrement()
    {
        strength -= 1;
    }

    void getdatac()
    {
        cout << "Enter Roll no :";
        cin >> roll_no;
        cout << "Enter Class :";
        cin >> cls;
        cout << "Enter Division :";
        cin >> division;
    }
};

int College::strength = 0;

class Student
{
private:
    string dob, name, bgrp;
    string contact_Address;
    long long int telephone_no;
    string drivingLicenseNo;

public:
    College c;

    Student()
    {
        dob = "";
        bgrp = "";
        contact_Address = "";
        telephone_no = 0;
        drivingLicenseNo = "";
    }

    Student(const Student &other)
    {
        dob = other.dob;
        bgrp = other.bgrp;
        contact_Address = other.contact_Address;
        telephone_no = other.telephone_no;
        drivingLicenseNo = other.drivingLicenseNo;
        c = other.c;
    }

    int rollNoCheck()
    {
        return c.roll_no;
    }

    void getdatas()
    {
        c.getdatac();
        cout << "Enter name:";
        cin >> name;
        cout << "Enter Date of birth:";
        cin >> dob;
        cout << "Enter Blood Group:";
        cin >> bgrp;
        cout << "Enter Contact Address:";
        cin.ignore(); // Added to clear the newline character from the input buffer
        getline(cin, contact_Address);
        cout << "Enter Telephone Number:";
        cin >> telephone_no;
        cout << "Enter Driving License number:";
        cin.ignore(); // Added to clear the newline character from the input buffer
        getline(cin, drivingLicenseNo);
        College::increment();
    }

    void display()
    {
        c.display();
        cout << "Date of Birth is:" << dob << endl;
        cout << "Blood Group is :" << bgrp << endl;
        cout << "Contact Address is:" << contact_Address << endl;
        cout << "Telephone Number:" << telephone_no << endl;
        cout << "Driving License number:" << drivingLicenseNo << endl;
        cout << "Total Number of student now " << College::strength << endl;
    }

    ~Student()
    {
        College::decrement();
        cout << "Student with roll_no " << c.roll_no << " is deleted\n";
        cout << "Total Number of student now " << College::strength << endl;
    }
};

int main()
{
    int n, i;

    cout << "Enter Number of students :";
    cin >> n;

    Student *s1[15];

    for (i = 0; i < n; i++)
    {
        cout << "\t\t" << i + 1 << endl;
        s1[i] = new Student;
        s1[i]->getdatas();
    }

    while (1)
    {
        int chc;

        cout << "1.Display all Student details\n";
        cout << "2.Delete a Particular student record\n";
        cout << "3.Add another record \n";
        cout << "4.End program\n";

        cin >> chc;

        switch (chc)
        {
        case 1:
            for (int j = 0; j < n; j++)
                s1[j]->display();
            break;

        case 2:
            int temroll;
            cout << "Enter roll no of student you want to delete: ";
            cin >> temroll;

            for (int j = 0; j < n; j++)
            {
                if (s1[j]->rollNoCheck() == temroll)
                {
                    delete s1[j];
                    // Shift elements to fill the empty space
                    for (int k = j; k < n - 1; k++)
                        s1[k] = s1[k + 1];
                    n--;
                    break;
                }
            }
            break;

        case 3:
            i++;
            n++;
            s1[i] = new Student;
            s1[i]->getdatas();
            break;

        case 4:
            return 0;
            break;
        }
    }

    return 0;
}
