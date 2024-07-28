import java.util.Scanner;

public class Priority {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of processes: ");
        int n = sc.nextInt();
        int p[] = new int[n];
        int bt[] = new int[n];
        int pt[] = new int[n];
        int at[] = new int[n];
        int wt[] = new int[n];
        int tat[] = new int[n];
        int ct[] = new int[n];
        double avgWT = 0, avgTAT = 0;

        int pos = 0, temp;

        for (int i = 0; i < n; i++) {
            System.out.print("Enter the arrival times: ");
            at[i] = sc.nextInt();
            System.out.print("Enter the burst times: ");
            p[i] = i + 1;
            bt[i] = sc.nextInt();
            System.out.print("Enter priority: ");
            pt[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            pos = i;
            for (int j = i + 1; j < n; j++) {
                if (pt[j] > pt[pos]) {
                    pos = j;
                }
            }
            temp = pt[pos];
            pt[pos] = pt[i];
            pt[i] = temp;

            temp = p[pos];
            p[pos] = p[i];
            p[i] = temp;

            temp = bt[pos];
            bt[pos] = bt[i];
            bt[i] = temp;

            temp = at[pos];
            at[pos] = at[i];
            at[i] = temp;
        }

        int currentTime = 0;

        for (int i = 0; i < n; i++) {
            if (currentTime < at[i]) {
                currentTime = at[i];
            }
            wt[i] = currentTime - at[i];
            currentTime += bt[i];
            tat[i] = currentTime - at[i];
            ct[i] = currentTime;

            avgTAT += tat[i];
            avgWT += wt[i];
        }

        System.out.println("");
        System.out.println("Process\tAT\tBT\tPriority\tCT\tWT\tTAT");

        for (int i = 0; i < n; i++) {
            System.out.println("P" + p[i] + "\t" + at[i] + "\t" + bt[i] + "\t" + pt[i] + "\t\t" + ct[i] + "\t" + wt[i]
                    + "\t" + tat[i]);
        }

        System.out.println("");
        System.out.println("Gantt Chart : ");
        System.out.println("");

        for (int i = 0; i < n; i++) {
            System.out.print(" -------- ");
        }
        System.out.println("");

        for (int i = 0; i < n; i++) {
            System.out.print("|   P" + p[i] + "   |");
        }

        System.out.println("");

        for (int i = 0; i < n; i++) {
            System.out.print(" -------- ");
        }
        System.out.println("");
        System.out.print("0");

        for (int i = 0; i < n; i++) {
            System.out.print("        " + ct[i]);
        }

        System.out.println("");

        avgWT /= n;
        avgTAT /= n;
        System.out.println("\nAverage Waiting Time: " + avgWT);
        System.out.println("Average Turn Around Time: " + avgTAT);
        sc.close();
    }
}
