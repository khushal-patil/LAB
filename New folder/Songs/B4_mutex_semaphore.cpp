#include<iostream>
using namespace std;
class synchronization
{
    int mutex=1;
    int empty=5;
    int full=0;
    int a[5];
    void signal(int &x){
        x++;
    }
    void wait(int &x){
        if(x>0){
            x--;
        }
    }
    public:
    void producer(){
        cout<<"Empty :"<<empty<<"Full :"<<full<<"Mutex :"<<mutex<<endl;
        if(empty!=0 && mutex==1){
            cout<<"Data to be produced is :";
            wait(empty);
            wait(mutex);
            cin>>a[full];
            cout<<"Data produced is :"<<a[full]<<endl;
            signal(mutex);
            signal(full);
        }
    }
      void consumer(){
        cout<<"Empty :"<<empty<<"Full :"<<full<<"Mutex :"<<mutex<<endl;
        if(full!=0 && mutex==1){
  
            wait(full);
            wait(mutex);
      
            cout<<"Data consumed is :"<<a[full]<<endl;
            signal(mutex);
            signal(empty);
        }
}    
};
int main(){
    int ch;
    synchronization s;
    do{
        cout<<"Menu"<<endl;
        cout<<"1.producer\n2.consumer\n3.exit\nenter choice :" ;
        cin>>ch;
        switch(ch)
        {
            case 1:
            s.producer();
            break;
            case 2:
            s.consumer();
            break;
            case 3:
            break;
            default:
            break;
        }
    }while(ch!=3);
    return 0;
}
