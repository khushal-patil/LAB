#include<iostream>
#include<vector>
#include<algorithm>
#include<string.h>
using namespace std;

class record{
	public:
		string name,dob,phone;
		
		void get(){
                cout<<endl;
				cout<<"Enter Name: ";
				cin>>name;
				cout<<"Enter DOB: ";
				cin>>dob;
				cout<<"Enter Phone: ";
				cin>>phone;
		}
		
		void display(){
			cout<<name<<"\t\t"<<dob<<"\t\t"<<phone<<endl;
		
		}
		
		bool operator < (const record& rhs){
			return name<rhs.name;
		}
		
		friend bool operator==(const record &r1, const record &r2){
			if(r1.name == r2.name||r1.dob==r2.dob||r1.phone==r2.phone){
				return true;
			}
			return false;
		}
};

class record_list{
	public:
		vector<record> myRecords;
		record r;
		void get(){
			int count;
			cout<<"Enter the Number of Students you want to add: ";
			cin>>count;
			for(int i=1;i<=count;i++){
		
				r.get();
				myRecords.push_back(r);
				r.display();
			}
		}
		
		void display(){
            cout<<endl;
			for(vector<record>::iterator itr=myRecords.begin();itr!= myRecords.end();itr++){
				itr->display;
			}
		}
		
		void search(string data){
			record rhs;
			rhs.name=data;
			rhs.dob=data;
			rhs.phone=data;
			vector<record>::iterator itr=find(myRecords.begin(),myRecords.end(),rhs);
			if(itr!=myRecords.end()){
				cout<<"Record Found.."<<endl;
				itr->display();
			}else{
				cout<<"Record not Found..."<<endl;
			}
        }
			
        void sort(){
			std::sort(myRecords.begin(),myRecords.end());	
		}

};

int main(){
	record_list r1;
	string key;
	
	int ch,chr;
	
	do{
            
			cout<<"\n1. Enter Details"<<endl;
			cout<<"2. Display"<<endl;
			cout<<"3. Search Entry"<<endl;
			cout<<"4. Sort Records"<<endl;
			cout<<"5. Exit"<<endl;
			cout<<"Enter Choice: ";
			cin>>ch;
			
			switch(ch){
				case 1:
						r1.get();
					break;
				case 2:
						r1.display();
					break;
				case 3:
						cout<<"Enter Either Name,DOB,Phone you want to find: ";
						cin>>key;
						r1.search(key);
					break;
				case 4:
						r1.sort();
						r1.display();
					break;
				case 5:
					cout<<"Thank You..."<<endl;
					break;
			}
	
	}while(ch!=5);
	return 0;
}