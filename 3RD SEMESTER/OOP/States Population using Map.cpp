#include<iostream>
#include<map>
#include<string>
using namespace std;

int main(){
    string state;
    int population;
    
    int ch;
    map<string,int> m;
    map<string,int>::iterator itr;

    do{
        cout<<"\nMenu: "<<endl;
        cout<<"1. Add State"<<endl;
        cout<<"2. Display States"<<endl;
        cout<<"3. Search State Population"<<endl;
        cout<<"4. Exit"<<endl;
        cout<<"Enter choice: ";
        cin>>ch;
        switch(ch){
            case 1:
                    cout<<"Enter the name of State: ";
                    cin>>state;
                    cout<<"Enter the Population(million): ";
                    cin>>population;
                    m.insert(pair<string,int>(state,population));
                    cout<<"State added"<<endl;
                    break;
            case 2:
                    cout<<"State and its Population-"<<endl;
                    for(itr = m.begin();itr!=m.end();itr++){
                        cout<<itr->first<<" States Population is "<<itr->second<<" million."<<endl;
                    }
                    cout<<endl;
                break;
            case 3:
                cout<<"\nEnter name of state for searching its population: ";
                cin>>state;
                if(m.count(state) != 0){
                    itr = m.find(state);
                    cout<<itr->first<<" States Population is "<<itr->second<<" million."<<endl;
                }else{
                    cout<<"States are not present in Map."<<endl;
                }
                
                
                break;
            case 4:
                cout<<"\nThank You..";
                break;
            default:
                cout<<"\nInvalid Choice.."<<endl;

        }

    }while(ch!=4);
return 0;
}