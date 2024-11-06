#include <iostream>
using namespace std;

void worstfit(int blocksize[], int m, int process_size[], int n) {
    int allocation[n];
    for (int i = 0; i < n; i++) {
        allocation[i] = -1;
        int worstIdx = -1;
        for (int j = 0; j < m; j++) {
            if (blocksize[j] >= process_size[i]) {
                if (worstIdx == -1 || blocksize[j] > blocksize[worstIdx]) {
                    worstIdx = j;
                }
            }
        }
        if (worstIdx != -1) {
            allocation[i] = worstIdx;
            blocksize[worstIdx] -= process_size[i];
        }
    }
    cout << "Process No.   Process Size   Block No.\n";
    for (int i = 0; i < n; i++) {
        cout << " " << i + 1 << "\t\t" << process_size[i] << "\t\t";
        if (allocation[i] != -1)
            cout << allocation[i] + 1;
        else
            cout << "not allocated";
        cout << endl;
    }
}

int main() {
    int m, n;
    cout << "Enter the number of blocks: ";
    cin >> m;
    int blocksize[m];
    cout << "Enter the sizes of the blocks:\n";
    for (int i = 0; i < m; i++) {
        cout << "Block " << i + 1 << ": ";
        cin >> blocksize[i];
    }

    cout << "Enter the number of processes: ";
    cin >> n;
    int process_size[n];
    cout << "Enter the sizes of the processes:\n";
    for (int i = 0; i < n; i++) {
        cout << "Process " << i + 1 << ": ";
        cin >> process_size[i];
    }

    worstfit(blocksize, m, process_size, n);
    return 0;
}
