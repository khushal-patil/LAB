import java.util.Scanner;

public class FirstFit {
    public static void main(String[] args) {
        final int MAX = 25;
        int[] frag = new int[MAX];
        int[] b = new int[MAX]; 
        int[] f = new int[MAX]; 
        int[] bf = new int[MAX]; 
        int[] ff = new int[MAX]; 
        int nb, nf, temp;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Memory Management - First Fit");

        System.out.print("Enter the number of blocks: ");
        nb = scanner.nextInt();
        
        System.out.print("Enter the number of files: ");
        nf = scanner.nextInt();

        System.out.println("Enter the size of the blocks:");
        for (int i = 0; i < nb; i++) {
            System.out.print("Block " + (i + 1) + ": ");
            b[i] = scanner.nextInt();
        }

        System.out.println("Enter the size of the files:");
        for (int i = 0; i < nf; i++) {
            System.out.print("File " + (i + 1) + ": ");
            f[i] = scanner.nextInt();
        }

        
        for (int i = 0; i < nb; i++) {
            bf[i] = 0;
        }

       
        for (int i = 0; i < nf; i++) {
            for (int j = 0; j < nb; j++) {
                if (bf[j] != 1) {
                    temp = b[j] - f[i];
                    if (temp >= 0) {
                        ff[i] = j;
                        frag[i] = temp;
                        bf[j] = 1;
                        break;
                    }
                }
            }
        }

       
        System.out.println("\nFile_no:\tFile_size:\tBlock_no:\tBlock_size:\tFragment");
        for (int i = 0; i < nf; i++) {
            System.out.printf("%d\t\t%d\t\t%d\t\t%d\t\t%d%n", 
                (i + 1), f[i], (ff[i] + 1), b[ff[i]], frag[i]);
        }

        scanner.close();
    }
}

