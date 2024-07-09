import java.util.*;

public class FCFS {

  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter No. of Processes: ");

    int n = sc.nextInt();

    int pno[] = new int[n];

    int ar[] = new int[n];

    int bt[] = new int[n];

    int ct[] = new int[n];

    int ta[] = new int[n];

    int wt[] = new int[n];

    int temp;

    float avgwt = 0;

    for (int i = 0; i < n; i++) {
      System.out.println("Enter Process " + (i + 1) + " Arrival Time: ");

      ar[i] = sc.nextInt();

      System.out.println("Enter Process " + (i + 1) + " Burst Time: ");

      bt[i] = sc.nextInt();

      pno[i] = i + 1;
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n - (i + 1); j++) {
        if (ar[j] > ar[j + 1]) {
          temp = ar[j];

          ar[j] = ar[j + 1];

          ar[j + 1] = temp;

          temp = bt[j];

          bt[j] = bt[j + 1];

          bt[j + 1] = temp;

          temp = pno[j];

          pno[j] = pno[j + 1];

          pno[j + 1] = temp;
        }
      }
    }

    for (int i = 0; i < n; i++) {
      if (i == 0) {
        ct[i] = ar[i] + bt[i];
      } else {
        if (ar[i] > ct[i - 1]) {
          ct[i] = ar[i] + bt[i];
        } else ct[i] = ct[i - 1] + bt[i];
      }

      ta[i] = ct[i] - ar[i];

      wt[i] = ta[i] - bt[i];

      avgwt += wt[i];
    }

    System.out.println(
      "\n P.No. \t Arrival Time \t Burst time \t Service time \t Waiting time"
    );

    for (int i = 0; i < n; i++) {
      System.out.println(
        "P" +
        pno[i] +
        " \t " +
        ar[i] +
        "\t\t" +
        bt[i] +
        "\t\t" +
        ct[i] +
        "\t\t" +
        wt[i]
      );
    }

    sc.close();

    System.out.println("");

    System.out.println("Gantt Chart : ");

    for (int i = 0; i < n; i++) {
      int c = 0;

      for (int j = 0; j < ct[i]; j++) {
        if (c == 0) {
          System.out.print("|____P" + pno[i] + " _");

          c = 1;
        } else {
          System.out.print("_");
        }
      }

      System.out.print(" |");
    }

    System.out.println("");

    for (int i = 0; i < n; i++) {
      int c = 0;

      for (int j = 0; j < ct[i]; j++) {
        if (c == 0) {
          System.out.print("\t" + ct[i]);

          c = 1;
        } else {
          System.out.print(" ");
        }
      }

      System.out.print(" |");
    }

    System.out.println("\n\n Average Waiting Time : " + (avgwt / n));
  }
}
