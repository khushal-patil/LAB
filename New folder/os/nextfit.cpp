#include <iostream>
using namespace std;

void nextFit(int blockSize[], int m, int processSize[], int n) {
    int allocation[n];
    int j = 0; // start from the first block

    for (int i = 0; i < n; i++) {
        allocation[i] = -1; // initially, no block is assigned

        // search for next fit
        int start = j;
        do {
            if (blockSize[j] >= processSize[i]) {
                allocation[i] = j;
                blockSize[j] -= processSize[i];
                break;
            }
            j = (j + 1) % m; // move to the next block circularly
        } while (j != start);
    }

    cout << "Process No.\tProcess Size\tBlock No.\n";
    for (int i = 0; i < n; i++) {
        cout << " " << i + 1 << "\t\t" << processSize[i] << "\t\t";
        if (allocation[i] != -1)
            cout << allocation[i] + 1;
        else
            cout << "Not Allocated";
        cout << endl;
    }
}

int main() {
    int m, n;

    // Taking input for the number of blocks and their sizes
    cout << "Enter the number of blocks: ";
    cin >> m;
    int blockSize[m];
    cout << "Enter the sizes of the blocks:\n";
    for (int i = 0; i < m; i++) {
        cout << "Block " << i + 1 << ": ";
        cin >> blockSize[i];
    }

    // Taking input for the number of processes and their sizes
    cout << "Enter the number of processes: ";
    cin >> n;
    int processSize[n];
    cout << "Enter the sizes of the processes:\n";
    for (int i = 0; i < n; i++) {
        cout << "Process " << i + 1 << ": ";
        cin >> processSize[i];
    }

    // Call the nextFit function with user inputs
    nextFit(blockSize, m, processSize, n);

    return 0;
}
