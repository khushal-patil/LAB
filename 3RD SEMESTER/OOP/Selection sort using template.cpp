#include<iostream>
using namespace std;

const int size = 10;
int n;
template<typename T>
void Selection(T a[size]) {
    int i, j;
    T temp;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (a[j] < a[i]) {
                temp = a[j];
                a[j] = a[i];
                a[i] = temp;
            }
        }
    }

    cout << "\nAfter Sorting is: ";
    for (i = 0; i < n; i++) {
        cout << a[i] << "\t";
    }
    cout << endl;
}

int main() {
    int i;
    int a[size];
    float b[size];

    cout << "How many integers: ";
    cin >> n;
    cout << "Enter values: ";
    for (i = 0; i < n; i++) {
        cin >> a[i];
    }

    Selection(a);

    cout << "How many floats: ";
    cin >> n;
    cout << "Enter values: ";
    for (i = 0; i < n; i++) {
        cin >> b[i];
    }

    Selection(b);

    return 0;
}
