#include <iostream>
using namespace std;

#define SIZE 10

class DEQUE
{
    int a[SIZE];
    int front, rear, count;

    public:
        DEQUE(){
            front = -1;
            rear = -1;
            count = 0;
        }

        void addBegin(int item){
            if (count == SIZE){
                cout << "\nInsertion is not possible, overflow!";
                return;
            }
            if (front == -1){
                front = rear = 0;
            }else{
                for (int i = rear; i >= front; i--){
                    a[i + 1] = a[i];
                }
                rear++;
            }
            a[front] = item;
            count++;
        }

        void addEnd(int item){
            if (count == SIZE){
                cout << "\nInsertion is not possible, overflow!";
                return;
            }
            if (front == -1){
                front = rear = 0;
            }else{
                rear++;
            }
            a[rear] = item;
            count++;
        }

        void deleteFront(){
            if (front == -1){
                cout << "Deletion is not possible: DEQUE is empty";
                return;
            }
            cout << "The deleted element is " << a[front];
            if (front == rear){
                front = rear = -1;
            }else{
                front++;
            }
            count--;
        }

        void deleteEnd(){
            if (front == -1){
                cout << "Deletion is not possible: DEQUE is empty";
                return;
            }
            cout << "The deleted element is " << a[rear];
            if (front == rear){
                front = rear = -1;
            }else{
                rear--;
            }
            count--;
        }

        void display(){
            if (front == -1){
                cout << "DEQUE is empty";
                return;
            }
            for (int i = front; i <= rear; i++){
                cout << a[i] << " ";
            }
            cout << endl;
        }
};

int main(){
    int choice, item;
    DEQUE d1;

    do{
        cout << "\n\n****DEQUE OPERATION****\n";
        cout << "1-Insert at beginning\n";
        cout << "2-Insert at end\n";
        cout << "3-Display\n";
        cout << "4-Deletion from front\n";
        cout << "5-Deletion from rear\n";
        cout << "6-Exit\n";
        cout << "Enter your choice (1-6): ";
        cin >> choice;

        switch (choice){
        case 1:
            cout << "Enter the element to be inserted: ";
            cin >> item;
            d1.addBegin(item);
            break;
        case 2:
            cout << "Enter the element to be inserted: ";
            cin >> item;
            d1.addEnd(item);
            break;
        case 3:
            d1.display();
            break;
        case 4:
            d1.deleteFront();
            break;
        case 5:
            d1.deleteEnd();
            break;
        case 6:
            cout << "Exiting the program\n";
            break;
        default:
            cout << "Invalid choice\n";
            break;
        }
    }while (choice != 6);
    return 0;
}
