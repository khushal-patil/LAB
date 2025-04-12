#include <iostream>
using namespace std;

class queue
{
    int data[20];
    int f, r;

public:
    queue(){
        f = -1;
        r = -1;
    }

    int isempty(){
        if (f == -1){
            return 1;
        }else{
            return 0;
        }
    }

    int isfull(){
        if (r >= 20){
            return 1;
        }else{
            return 0;
        }
    }

    void enqueue(int x){
        if (isfull() == 1){
            cout << "job queue is full" << endl;
        }else{
            if (f == -1)
                f++;
            r++;
            data[r] = x;
        }
    }
    
    void dequeue(){
        int x;
        if (isempty()){
            cout << "job queue is empty" << endl;
        }else{
            x = data[f];
            f++;
            cout << x << "Job deleted " << endl;
        }
    }

    void disp(){
        cout << "job queue is as :" << endl;
        for (int i = f; i <= r; i++){
            cout << data[i] << " ";
        }
        cout << endl;
    }
};

int main()
{
    int ch, n, x, d;
    queue q;
    cout << "Enter the no. of jobs in queue. " << endl;
    cin >> n;
    cout << "Enter jobs " << endl;
    for (int i = 0; i < n; i++){
        cin >> d;
        q.enqueue(d);
    }
    do{
        cout << "**********MENU**********" << endl;
        cout << "1)Add job " << endl;
        cout << "2)Delete job " << endl;
        cout << "3)Display" << endl;
        cout << endl;
        cout << "Enter your choice " << endl;
        cin >> ch;

        switch (ch){
        case 1:
            cout << "Enter the job to be added " << endl;
            cin >> d;
            q.enqueue(d);
            cout << "Job added" << endl;
            q.disp();
            break;
        case 2:
            q.dequeue();
            q.disp();
            break;
        case 3:
            q.disp();
            break;
        default:
            cout << "Invalid choice" << endl;
            break;
        }
        cout << "Do you want to continue" << endl;
        cout << "1. YES" << endl;
        cout << "2. NO" << endl;
        cin >> x;

    } while (x == 1);
}

