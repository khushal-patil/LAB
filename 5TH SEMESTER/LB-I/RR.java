import java.util.*;

class Process {
    int processID;
    int arrival, burst, waiting, turnAround, remainingTime;
    int finish, completionTime;
}

public class RR {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("*** RR Scheduling (Preemptive) ***");

        System.out.print("Enter Number of Processes: ");
        int n = sc.nextInt();
        Process[] p = new Process[n];
        int sumBurst = 0;

        for (int i = 0; i < n; i++) {
            p[i] = new Process();
            p[i].processID = i + 1;
            System.out.print("Enter the arrival time for P" + (i + 1) + ": ");
            p[i].arrival = sc.nextInt();
            System.out.print("Enter the burst time for P" + (i + 1) + ": ");
            p[i].burst = sc.nextInt();
            p[i].remainingTime = p[i].burst;
            p[i].finish = 0;
            sumBurst += p[i].burst;
            System.out.println();
        }

        System.out.print("Enter time quantum: ");
        int quantum = sc.nextInt();

        Arrays.sort(p, Comparator.comparingInt(proc -> proc.arrival));

        Queue<Integer> q = new LinkedList<>();
        int time = 0;
        double avgWAT = 0, avgTAT = 0;
        List<String> ganttChart = new ArrayList<>();
        List<Integer> ganttTimeLabels = new ArrayList<>();

        System.out.println("\nGantt Chart:");

        // Add initial processes to the queue based on arrival time
        for (int i = 0; i < n; i++) {
            if (p[i].arrival <= time) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            Integer I = q.poll();
            int i = I.intValue();

            int executionTime = Math.min(quantum, p[i].remainingTime);
            p[i].remainingTime -= executionTime;
            time += executionTime;

            ganttChart.add("P" + p[i].processID);
            ganttTimeLabels.add(time - executionTime);

            if (p[i].remainingTime <= 0) {
                p[i].finish = 1;
                p[i].completionTime = time;
                p[i].turnAround = p[i].completionTime - p[i].arrival;
                p[i].waiting = p[i].turnAround - p[i].burst;
                avgTAT += p[i].turnAround;
                avgWAT += p[i].waiting;
            } else {
                // Add the current process back to the queue if it hasn't finished
                q.add(i);
            }

            // Add new processes to the queue based on arrival time
            for (int j = 0; j < n; j++) {
                if (p[j].arrival <= time && p[j].finish == 0 && !q.contains(j) && j != i) {
                    q.add(j);
                }
            }
        }
        ganttTimeLabels.add(time);

        // Print the Gantt chart
        for (String process : ganttChart) {
            System.out.print(" -------- ");
        }
        System.out.println();

        for (String process : ganttChart) {
            System.out.print("|   " + process + "   |");
        }
        System.out.println();

        for (String process : ganttChart) {
            System.out.print(" -------- ");
        }
        System.out.println();

        for (int t : ganttTimeLabels) {
            System.out.print(String.format("%-10s", t));
        }
        System.out.println();

        System.out.println("\nProcess\t\tArrival\t\tBurst\t\tCompletion\tTurnaround\tWaiting");
        for (int i = 0; i < n; i++) {
            System.out.println("P" + p[i].processID + "\t\t" + p[i].arrival + "\t\t" + p[i].burst + "\t\t"
                    + p[i].completionTime + "\t\t" + p[i].turnAround + "\t\t" + p[i].waiting);
        }

        System.out.println("\nAverage turnaround time: " + (avgTAT / n) + " ms");
        System.out.println("Average waiting time: " + (avgWAT / n) + " ms");

        sc.close();
    }
}
