#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

struct Process {
    int id;       // Process ID
    int burst;    // Burst Time
};

// Function to find waiting time for each process
void findWaitingTime(Process processes[], int n, int wt[])
{
    wt[0] = 0; // Waiting time for the first process is 0
    for (int i = 1; i < n; i++)
    {
        wt[i] = processes[i - 1].burst + wt[i - 1];
    }
}

// Function to calculate turnaround time
void findTurnAroundTime(Process processes[], int n, int wt[], int tat[])
{
    for (int i = 0; i < n; i++)
    {
        tat[i] = processes[i].burst + wt[i];
    }
}

// Function to find average waiting and turnaround time, and display Gantt chart
void findAverageTime(Process processes[], int n)
{
    int wt[n], tat[n], total_wt = 0, total_tat = 0;

    // Sort processes based on burst time for SJF
    sort(processes, processes + n, [](Process a, Process b) { return a.burst < b.burst; });

    findWaitingTime(processes, n, wt);
    findTurnAroundTime(processes, n, wt, tat);

    cout << "\nProcess\tBurst Time\tWaiting Time\tTurnaround Time\n";
    for (int i = 0; i < n; i++)
    {
        total_wt += wt[i];
        total_tat += tat[i];
        cout << "  " << processes[i].id << "\t\t" << processes[i].burst << "\t\t" << wt[i] << "\t\t" << tat[i] << endl;
    }

    cout << "\nAverage Waiting Time: " << (float)total_wt / n;
    cout << "\nAverage Turnaround Time: " << (float)total_tat / n;

    cout << "\n\nGantt Chart:\n";
    for (int i = 0; i < n; i++)
    {
        cout << "|  P" << processes[i].id << "  ";
    }
    cout << "|\n";

    int time = 0;
    for (int i = 0; i < n; i++)
    {
        cout << time << setw(6) << "";
        time += processes[i].burst;
    }
    cout << time << endl;
}

int main()
{
    int n;
    cout << "Enter total number of processes: ";
    cin >> n;
    Process processes[n];
    cout << "\nEnter burst time for each process:\n";
    for (int i = 0; i < n; i++)
    {
        processes[i].id = i + 1;
        cout << "P" << processes[i].id << ": ";
        cin >> processes[i].burst;
    }
    findAverageTime(processes, n);
    return 0;
}