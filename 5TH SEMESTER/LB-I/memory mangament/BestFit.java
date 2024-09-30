import java.util.Scanner;

public class BestFit {

    public static void main(String[] args) {
        final int MAX = 25;
        int[] frag = new int[MAX];
        int[] b = new int[MAX]; 
        int[] f = new int[MAX]; 
        int[] bf = new int[MAX]; 
        int[] ff = new int[MAX]; 

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number of blocks:");
        int nb = scanner.nextInt();
        System.out.println("Enter the number of files:");
        int nf = scanner.nextInt();

        System.out.println("\nEnter the size of the blocks:");
        for (int i = 1; i <= nb; i++) {
            System.out.printf("Block %d: ", i);
            b[i] = scanner.nextInt();
        }

        System.out.println("Enter the size of the files:");
        for (int i = 1; i <= nf; i++) {
            System.out.printf("File %d: ", i);
            f[i] = scanner.nextInt();
        }

        for (int i = 1; i <= nf; i++) {
            int lowest = 10000;
            int temp = 0;
            int bestBlock = -1;
            for (int j = 1; j <= nb; j++) {
                if (bf[j] != 1) {
                    temp = b[j] - f[i];
                    if (temp >= 0 && lowest > temp) {
                        lowest = temp;
                        bestBlock = j;
                    }
                }
            }
            frag[i] = lowest;
            ff[i] = bestBlock;
            if (bestBlock != -1) {
                bf[bestBlock] = 1;
            }
        }

        System.out.printf("\nFile No\tFile Size\tBlock No\tBlock Size\tFragmentation\n");
        for (int i = 1; i <= nf; i++) {
            if (ff[i] != 0) {
                System.out.printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n",
                        i, f[i], ff[i], b[ff[i]], frag[i]);
            }
        }

        scanner.close();
    }
}

