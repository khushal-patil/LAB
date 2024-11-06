#include <bits/stdc++.h>

using namespace std;

class Process {
public:
    int id, burst, arrival;
};

void RoundRobin(Process processes[], int n,int quantum, int wt[], int ct[], int tat[])
{
    queue<int> RQ;
    int currentTime = 0, completedTasks = 0;
    int remainingTime[n];
    int curr;

    for(int j =0; j < n; j++)
    {
        if (processes[j].arrival <= currentTime)
        {
            RQ.push(j);
        }
    }

    for (int i = 0; i < n; i++)
        remainingTime[i] = processes[i].burst;
    
    while (completedTasks != n) {
        
        curr = RQ.front();
        RQ.pop();

        int cntr = 0;

        while (cntr != quantum && cntr != remainingTime[curr]){
            currentTime++;
            cntr++;

            for (int j =0; j < n; j++){
                if (processes[j].arrival == currentTime)
                    RQ.push(j);
            }
        }
        remainingTime[curr] -= cntr;

        if (remainingTime[curr] == 0){
            ct[curr] = currentTime;
            tat[curr] = ct[curr] - processes[curr].arrival;
            completedTasks++;
            wt[curr] = ct[curr] - processes[curr].arrival - processes[curr].burst;
        }
        else{
            RQ.push(curr);
        }
    }
}

int main(){
    int n, quantum;
    cout << "Enter the number of processes: ";
    cin >> n;

    Process*proc = new Process[n];

    for(int i = 0; i < n; i++){
        proc[i].id = i + 1;
        cout << "Enter arrival time and burst time fpr process " << endl;
        cin >> proc[i].arrival >> proc[i].burst;
    }
    cout << "Enter the time quantum: ";
    cin >> quantum;

    int wt[n], ct[n], tat[n];
    fill(wt, wt + n, 0);

    RoundRobin(proc, n, quantum, wt, ct, tat);
    cout.width(5);
    cout << "ID";
    cout.width(5);
    cout << "AT";
    cout.width(5);
    cout << "BT";
    cout.width(5);
    cout << "CT";
    cout.width(5);
    cout << "TAT";
    cout.width(5);
    cout << "TAT" << endl;

    for (int i = 0; i < n; i++)
    {
        cout.width(5);
        cout << proc[i].id;
        cout.width(5);
        cout << proc[i].arrival;
        cout.width(5);
        cout << ct[i];
        cout.width(5);
        cout << tat[i];
        cout.width(5);
        cout << wt[i] << endl;
    }
    delete[] proc;
    return 0;
    
}