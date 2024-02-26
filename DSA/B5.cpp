#include<iostream>
#include<string.h>

using namespace std;

struct node{
	string label;
	int ch_count;
	
	struct node* child[10];
	
}*root;

class GT{

	public:
		
		GT(){
			
			root = NULL;
		}
		
		string lbel;
		int count;
		
		void create(){
		
				
				root = new node;
				
				cout<<"Enter the Name of Book: ";
				cin>>root->label;
				cout<<"Enter No. of Chapters: ";
				cin>>root->ch_count;
					
				
				for(int i=0;i<root->ch_count;i++){
				
					root->child[i] = new node;
					cout<<"Enter the "<< i+1 <<" Name of Chapter: ";
					cin>>root->child[i]->label;
					cout<<"Enter the No of Sections: ";
					cin>>root->child[i]->ch_count;

					for(int j=0;j<root->child[i]->ch_count;j++){
						root->child[i]->child[j] = new node;
						cout<<"Enter the "<< i+1 <<" - "<< j+1<< " Name of Sections: ";
						cin>>root->child[i]->child[j]->label;
						cout<<"Enter the No of Sub-Section: ";
						cin>>root->child[i]->child[j]->ch_count;
						
						for(int k=0;k<root->child[i]->child[j]->ch_count;k++){
							root->child[i]->child[j]->child[k] = new node;
							cout<<"Enter the "<< i+1 <<" - "<< j+1<< " - "<< k+1<< " Name of Sub Section: ";
							cin>>root->child[i]->child[j]->label;
						
						}
					}
					
					
				}
			
			
		} 
		
		void display(node * r){
				cout<<"\nName of Book: ";
				cout<<root->label<<endl;
				cout<<"No. of Chapters: ";
				cout<<root->ch_count<<endl;
			
				for(int i=0;i<root->ch_count;i++){
					
						
						cout<<"\n Name of Chapter: ";
						cout<<root->child[i]->label<<endl;
						cout<<"	No of Sections: ";
						cout<<root->child[i]->ch_count<<endl;

						for(int j=0;j<root->child[i]->ch_count;j++){
							
							cout<<"\t\t"<< i+1 <<" - "<< j+1<< " Name of Sections: ";
							cout<<root->child[i]->child[j]->label<<endl;
							cout<<"\t\tNo of Sub-Section: ";
							cout<<root->child[i]->child[j]->ch_count<<endl;
							
							for(int k=0;k<root->child[i]->child[j]->ch_count;k++){
								
								cout<<"\t\t\t"<< i+1 <<" - "<< j+1<< " - "<< k+1<< " Name of Sub Section: ";
								cout<<root->child[i]->child[j]->label<<endl;
							
							}
						}
				
			}
		
		}


};


int main(){
	GT g;
	
	while(1){
		cout<<"******* Book Information *******"<<endl;
		cout<<"1. Add Book Info."<<endl;
		cout<<"2. Display."<<endl;
		cout<<"3. Exit"<<endl;
		cout<<"Enter Choice: ";
		int ch;
		cin>>ch;

		switch(ch){
			case 1:
				g.create();
				break;
			case 2:
				g.display(root);
				break;
			case 3:
				exit(0);
				break;
			default:
				cout<<"Invalid Choice....";
				break;
		}
	}
}
