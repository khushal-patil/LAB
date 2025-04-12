#include <iostream>
#include <string.h>
using namespace std;

int top;
char str[20];

void push(char a){
    top++;
    str[top]=a;
}

void pop(){
    top--;
}
void input(){
    char ch[20];
    int x=1,i=0;
    top=-1;
    cout<<"\n Enter the Expression: ";
    cin>>ch;
    while(i<strlen(ch)){
        if((ch[i]=='{') || (ch[i]=='[')||(ch[i]=='(')){
            push(ch[i]);
        }
        if(ch[i]=='}'){
            if(str[top]=='{'){
                pop();
            }else{
                cout<<"\n '{' absent"<<endl;
            }
        }

        if(ch[i]==']'){
            if(str[top]=='['){
                pop();
            }else{
                cout<<"\n '[' absent"<<endl;
            }
        }

          if(ch[i]==')'){
            if(str[top]=='('){
                pop();
            }else{
                cout<<"\n '(' absent"<<endl;

            }
        }

        i++;
    }

    if(top==-1){
        x=5;
        cout<<"\nStack Empty.."<<endl;
        cout<<"\nExpression is well paranthesized"<<endl;
    }else{
        while(top!=-1){
            if(str[top]=='['){
                pop();
                cout<<"\n ']' absent";
            }
             if(str[top]=='{'){
                pop();
                cout<<"\n '}' absent";
            }
             if(str[top]=='('){
                pop();
                cout<<"\n ')' absent";
            }

            cout<<"\n Expression is not well paranthesized...";
        }
    }
}

int main(){
    input();
    return 0;
}