//Round robin:
#include<iostream>
using namespace std;
class rr {
public:
    string pr[20];         
    int n, tq, bt[20], at[20], tempbt[20], ttime[20], k;
    string temp[20];       
    int comp_time[20];     
    void ganttchart() {
        string remainpr[20];
        int remainbt[20], btime;
        tempbt[0] = 0;
        for (int i = 0; i < n; i++) remainpr[i] = pr[i];
        for (int i = 0; i < n; i++) remainbt[i] = bt[i];
        int time = 0;
        int idx = 0;  // index for the temp array
        while (true) {
            bool done = true;
            for (int i = 0; i < n; i++) {
                if (remainbt[i] > 0) {
                    done = false;
                    if (remainbt[i] <= tq) {
                        temp[idx] = remainpr[i];  
                        time += remainbt[i];  
                        tempbt[idx + 1] = time;
                        remainbt[i] = 0;  
                        comp_time[i] = time;  
                        idx++;
                    } else {
                        temp[idx] = remainpr[i];  
                        time += tq;  
                        tempbt[idx + 1] = time;
                        remainbt[i] -= tq;
                        idx++;
                    }
                }
            }
            if (done) break;  // Exit if all processes are done
        }

        // Print the Gantt chart
        cout << "\nGantt Chart\n   ";
        for (int i = 0; i < idx; i++) {
            cout << temp[i] << "      ";  // Print process names
        }
        cout << endl;
        for (int i = 0; i <= idx; i++) {
            cout << tempbt[i] << "      ";  // Print time slots
        }
    }
     void turnaround() {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            // Turnaround time = Completion time - Arrival time
            int tt = comp_time[i] - at[i];
            ttime[i] = tt;
            sum += tt;
            cout << "Turnaround time of " << pr[i] << " is: " << tt << endl;
        }
        cout << "\nAverage turnaround time = " << (float)sum / n << endl;
    }
    void printTable() {
        cout << "\nProcess ID | Arrival Time | Burst Time | Turnaround Time\n";
        cout << "----------------------------------------------------------\n";
        for (int i = 0; i < n; i++) {
            cout << pr[i] << "          | " << at[i] << "            | " << bt[i] << "         | " << ttime[i] << endl;
        }
    }
};
int main() {
    rr obj;
    cout << "ROUND ROBIN\nEnter total number of processes: ";
    cin >> obj.n;
    for (int i = 0; i < obj.n; i++) {
        cout << "Enter process[" << i + 1 << "]: ";
        cin >> obj.pr[i];
        cout << "Enter Arrival Time of " << obj.pr[i] << ": ";
        cin >> obj.at[i];
        cout << "Enter Burst Time of " << obj.pr[i] << ": ";
        cin >> obj.bt[i];
    }
    cout << "Enter time quantum: ";
    cin >> obj.tq;
    obj.ganttchart();    // Generate Gantt chart
    obj.turnaround();    // Calculate and print turnaround times
    obj.printTable();    // Print process table
    return 0;
}
