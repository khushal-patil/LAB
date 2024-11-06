//SJF:
#include<iostream>
#include<string.h>
using namespace std;

void SJF_pre(int n, int BT[], string p[], int AT[]) {
    int Finish_time[10], TA[10], WT[10];
    float avgTA = 0, avgWT = 0;
    for (int i = 0; i < n; i++) {
        Finish_time[i] = (i == 0) ? BT[i] + AT[i] : BT[i] + Finish_time[i - 1];
        TA[i] = Finish_time[i] - AT[i];
        avgTA += TA[i];
    }
    cout << "\n---------------------------------------------------------------\n";
    cout << "| Process | Arrival Time | Burst Time | Turnaround Time |\n";
    cout << "---------------------------------------------------------------\n";
    for (int i = 0; i < n; i++) {
        cout << "|   " << p[i] << "   |     " << AT[i] << "      |     " << BT[i] << "     |       " << TA[i] << "         |\n";
        WT[i] = TA[i] - BT[i];
        avgWT += WT[i];
    }
    cout << "---------------------------------------------------------------\n";
    cout << "Average Turnaround Time = " << avgTA / n << " msec\n";
    for (int i = 0; i < n; i++) cout << "Waiting time of " << p[i] << " = " << WT[i] << " msec\n";
    cout << "Average Waiting Time = " << avgWT / n << " msec\n";
    cout << "\nGantt Chart:\n-----------------------------------\n";
    for (int i = 0; i < n; i++) cout << "|  " << p[i] << "  ";
    cout << "|\n0";
    for (int i = 0; i < n; i++) cout << "    " << Finish_time[i];
    cout << endl;
}

int main() {
    int n, BT[10], AT[10];
    string p[10];
    cout << "Enter the number of processes: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Enter process name: ";
        cin >> p[i];
        cout << "Enter Burst time: ";
        cin >> BT[i];
        cout << "Enter Arrival time: ";
        cin >> AT[i];
    }
    SJF_pre(n, BT, p, AT);
    return 0;
}

