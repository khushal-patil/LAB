//FCFS:
#include<iostream>
#include<algorithm>
using namespace std;

struct Process {
    int id, bt, at, wt, tat, ct, start_time;
};

bool compareArrivalTime(Process p1, Process p2) {
    return p1.at < p2.at;
}

int main() {
    int n;
    float avg_tat = 0, avg_wt = 0;
    cout<<"Enter no. : ";
    cin >> n;
    Process p[n];

    for (int i = 0; i < n; i++) {
        p[i].id = i + 1;
        cout<<"Enter bt for process "<<i+1<<" : ";
        cin >> p[i].bt;
        cout<<"Enter at for process "<<i+1<<" : ";
        cin >> p[i].at;
    }

    sort(p, p + n, compareArrivalTime);

    p[0].start_time = p[0].at;
    p[0].ct = p[0].start_time + p[0].bt;
    p[0].tat = p[0].ct - p[0].at;
    p[0].wt = p[0].tat - p[0].bt;

    for (int i = 1; i < n; i++) {
        p[i].start_time = max(p[i - 1].ct, p[i].at);
        p[i].ct = p[i].start_time + p[i].bt;
        p[i].tat = p[i].ct - p[i].at;
        p[i].wt = p[i].tat - p[i].bt;
    }

    cout << "\nProcess ID | Arrival Time | Burst Time | Turnaround Time | Waiting Time\n";
    for (int i = 0; i < n; i++) {
        cout << "P" << p[i].id << "    | " << p[i].at << "         | " << p[i].bt
             << "        | " << p[i].tat << "           | " << p[i].wt << endl;
    }

    cout << "\nGantt chart:\n";
    for (int i = 0; i < n; i++) cout << "p" << p[i].id << " |";
    cout << endl;
    for (int i = 0; i < n; i++) cout << p[i].start_time << "\t";
    cout << p[n-1].ct << endl;

    for (int i = 0; i < n; i++) {
        avg_wt += p[i].wt;
        avg_tat += p[i].tat;
    }

    cout << "\nAverage turnaround time is: " << avg_tat / n;
    cout << "\nAverage waiting time is: " << avg_wt / n;

    return 0;
}

