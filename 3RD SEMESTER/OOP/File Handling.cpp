#include<iostream>
 #include<fstream>
 using namespace std;

 class student{
    char Name[20];
    int Rollno;
    char stclass[20];

    public:
        void accept(){
            cout<<"Enter Name: ";
            cin>>Name;
            cout<<"Enter Roll No: ";
            cin>>Rollno;
            cout<<"Enter Class: ";
            cin>>stclass;
        }

        void display(){
            cout<<"\n Name: "<<Name;
            cout<<"\n Roll No: "<<Rollno;
            cout<<"\n Class: "<<stclass<<"\n";

        }
 };
 
 int main(){

    int i,n;
    cout<<"How many students information you want to add: ";
    cin>>n;
    student s[n];
    fstream f;
    
    f.open("studinfo.txt");
    for(int i=0;i<n;i++){
        cout<<"\nStudent Details: "<<i+1<<endl;
        s[i].accept();
        f.write((char*)&s[i],sizeof s[i]);
    }
    f.close();

    cout<<"\nInformation of File: "<<endl;
    f.open("studinfo.txt",ios::in);
    for(int i=0;i<n;i++){
        cout<<"\nStudent: "<<i+1;
        f.read((char*) &s[i],sizeof s[i]);
        s[i].display();
    }
    f.close();
	return 0;
 }