#include <iostream>
#include <fstream>
using namespace std;

struct student {
    int rollNo;
    char name[50];
    char div[30];
    char address[100];
};

class StudentDatabase {
    string fileName = "student_data12.dat";

public:
    StudentDatabase() {
        fstream fileObj(fileName);
        if (fileObj.fail()) {
            fileObj.open(fileName, ios::out);
            cout << "New File Created" << endl;
        } else {
            cout << "Existing File Found" << endl;
        }
    }

    void addStudent();
    void searchOrDelete(bool isDelete);
    void displayAll();
};

void StudentDatabase::addStudent() {
    student s;
    cout << "Enter Roll number, Name, Division, and Address of student:";
    cin >> s.rollNo;
    cin.ignore();
    cin.getline(s.name, 50);
    cin >> s.div;
    cin.ignore();
    cin.getline(s.address, 100);
    ofstream file(fileName, ios::out | ios::binary | ios::app);
    file.write((char*)&s, sizeof(student)) << flush;
    cout << "Student record added successfully" << endl;
    file.close();
}

void StudentDatabase::searchOrDelete(bool isDelete) {
    int roll;
    student s;
    bool found = false;
    cout << "Enter roll number:";
    cin >> roll;
    ifstream readFile(fileName, ios::in | ios::binary);
    ofstream writeFile("~" + fileName, ios::out | ios::binary);
    while (readFile.read((char*)&s, sizeof(student))) {
        if (s.rollNo == roll) {
            found = true;
            if (!isDelete) {
                cout << "Found record with details\nRoll No:" << s.rollNo << "\nName:" << s.name << "\nDivision:" << s.div << "\nAddress:" << s.address << endl;
            }
        } else {
            writeFile.write((char*)&s, sizeof(student)) << flush;
        }
    }
    readFile.close();
    writeFile.close();
    if (isDelete) {
        if (found) {
            remove(fileName.c_str());
            rename(("~" + fileName).c_str(), fileName.c_str());
            cout << "Deleted record" << endl;
        } else {
            cout << "No record found" << endl;
        }
    }
}

void StudentDatabase::displayAll() {
    ifstream file(fileName, ios::in | ios::binary);
    student s;
    int count = 0;
    while (file.read((char*)&s, sizeof(student))) {
        count++;
        cout << count << ") " << s.rollNo << "|" << s.name << "|" << s.div << "|" << s.address << endl;
    }
    if (count == 0) {
        cout << "No records Found" << endl;
    }
    file.close();
}

int main() {
    int choice;
    StudentDatabase db;
    do {
        cout << "\nMENU\n1. Add Record\n2. Delete Record\n3. Search Record\n4. Display All Records\n0. Exit\nEnter Your Choice:";
        cin >> choice;
        switch (choice) {
            case 1: db.addStudent(); break;
            case 2: db.searchOrDelete(true); break;
            case 3: db.searchOrDelete(false); break;
            case 4: cout << "Records in File are\n"; db.displayAll(); break;
            case 0: cout << "Thank You" << endl; break;
            default: cout << "Enter a valid Choice" << endl; break;
        }
    } while (choice != 0);
    return 0;
}
