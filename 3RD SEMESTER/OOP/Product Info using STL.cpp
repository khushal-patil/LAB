#include<iostream>
#include<vector>
#include<algorithm>
#include<string.h>
using namespace std;

class item{
	public:
		string name;
		int itmcode;
		float cost;
		int quantity;
		
		void get(){
                cout<<endl;
				cout<<"Enter Name: ";
				cin>>name;
				cout<<"Enter Cost: ";
				cin>>cost;
				cout<<"Enter Quantity: ";
				cin>>quantity;
				cout<<"Enter Item Code: ";
				cin>>itmcode;
		}
		
		void display(){
			cout<<"Name: "<<name<<endl;
			cout<<"Cost: "<<cost<<endl;
			cout<<"Quantity: "<<quantity<<endl;
			cout<<"Item Code: "<<itmcode<<endl<<endl;
		}
		
		bool operator < (const item& rhs){
			return name<rhs.name;
		}
		
		friend bool operator==(const item &r1, const item &r2){
			if(r1.itmcode == r2.itmcode){
				return true;
			}
			return false;
		}
};

class item_list{
	public:
		vector<item> myList;
		item r;
		void get(){		
				r.get();
				myList.push_back(r);
				cout<<"Item Added."<<endl;
	
		}
		
		void display(){
            cout<<endl;
			for(vector<item>::iterator itr=myList.begin();itr!= myList.end();itr++){
				itr->display();
			}
		}
		
		void search(int data){
			item rhs;
			rhs.itmcode=data;
			
			vector<item>::iterator itr=find(myList.begin(),myList.end(),rhs);
			if(itr!=myList.end()){
				cout<<"Record Found.."<<endl;
				itr->display();
			}else{
				cout<<"Record not Found..."<<endl;
			}
        }
			
        void sort(){
			std::sort(myList.begin(),myList.end());	
		}

};

int main(){
	item_list i;
	int key;
	
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
						i.get();
					break;
				case 2:
						i.display();
					break;
				case 3:
						cout<<"Enter Item Code you want to find: ";
						cin>>key;
						i.search(key);
					break;
				case 4:
						i.sort();
						i.display();
					break;
				case 5:
					cout<<"Thank You..."<<endl;
					break;
			}
	
	}while(ch!=5);
	return 0;
}