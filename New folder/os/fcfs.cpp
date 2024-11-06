#include <iostream>
#include <iomanip>

using namespace std;

void findWaitingTime(int processes[], int n, int bt[], int wt[])
{
    wt[0] = 0;
    for (int i = 1; i < n; i++)
    {
        wt[i] = bt[i - 1] + wt[i - 1];
    }
}

void findTurnAroundTime(int processes[], int n, int bt[], int wt[], int tat[])
{
    for (int i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i];
    }
}

void findAverageTime(int processes[], int n, int bt[])
{
    int wt[n], tat[n], total_wt = 0, total_tat = 0;

    findWaitingTime(processes, n, bt, wt);
    findTurnAroundTime(processes, n, bt, wt, tat);

    for (int i = 0; i < n; i++)
    {
        total_wt += wt[i];
        total_tat += tat[i];
        cout << "  " << processes[i] << "\t\t" << bt[i] << "\t\t" << wt[i] << "\t\t" << tat[i] << endl;
    }
    cout << "\naverage waiting time: " << (float)total_wt / n;
    cout << "\naverage turn around time: " << (float)total_tat / n;

    cout << "\nGantt Chart\n";
    int time = 0;
    for (int i = 0; i < n; i++)
    {
        cout << time << setw(6) << "|  P" << processes[i] << "  ";
        time += bt[i];
    }
    cout << time << endl;
}

int main()
{
    int n;
    cout << "Enter total number of processes: ";
    cin >> n;
    int processes[n], bt[n];
    cout << "\nEnter burst time for each process: ";
    for (int i = 0; i < n; i++)
    {
        processes[i] = i + 1;
        cin >> bt[i];
    }
    findAverageTime(processes, n, bt);
}
