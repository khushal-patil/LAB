#include<iostream>
#include<ctype.h>
using namespace std;

class stack
{
    int top;
    char data[20];
    public:
    stack()
    {
        top=-1;
    }

    void  conversion(char infix[20],char postfix[20])
    {
         int j=0,i;
         char e,token,x;
         for(i=0;infix[i]!='\0';i++)
         {  
             token=infix[i];
             if(isalnum(token))
             {
                 postfix[j]=token;
                 j++;
             }
             else
             {
                 if(token=='(')
                     push(token);
                 else if(token==')')
                 {
                     while((x=pop())!='(')
                     {
                         postfix[j]=x;
                         j++;
                     }
                 }
                 else
                 {
                     e=topmost();
                     while(precedence(token)<=precedence(e) && !empty())
                     {
                         x=pop();
                         postfix[j]=x;
                         j++;
                     }
                     push(token);
                 }
             }
         }
         while(!empty())
         {
             x=pop();
             postfix[j]=x;
             j++;
         }
         postfix[j]='\0';
    }

    void push(int x)
    {
        top++;
        data[top]=x;
    }

    int pop()
    {
        char x;
        x=data[top];
        top--;
        return x;
    }

    char topmost()
    {
        char e;
        e=data[top];
        return e;
    }

    int precedence(char x)
    {
        if(x=='(')
            return 0;
        if(x=='+'|| x=='-')
            return 1;
        if(x=='*'|| x=='/' ||x=='%')
            return 2;
        else
            return 3;
    }

    int empty()
    {
        if(top==-1)
            return 1;
        else
            return 0;
    }
};
int main()
{
    stack s;
    char infix[20],postfix[20];
    cout<<"Enter the infix expression: ";
    cin>>infix;
    s.conversion(infix,postfix);
    cout<<"Post fix expression is:  "<<postfix;
    return 0;
}