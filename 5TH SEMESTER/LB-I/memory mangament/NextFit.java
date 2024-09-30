import java.util.Scanner;

public class NextFit {
    static final int max = 25;

    public static void main(String[] args) {
        int[] frag = new int[max];
        int[] b = new int[max];
        int[] f = new int[max]; 
        boolean[] bf = new boolean[max]; 
        int[] ff = new int[max];

        Scanner scanner = new Scanner(System.in);

        System.out.println("\n\tMemory Management Scheme - Next Fit");
        System.out.print("Enter the number of blocks: ");
        int nb = scanner.nextInt(); 
        System.out.print("Enter the number of files: ");
        int nf = scanner.nextInt(); 

        System.out.println("\nEnter the size of the blocks:-");
        for (int i = 1; i <= nb; i++) {
            System.out.print("Block " + i + ": ");
            b[i] = scanner.nextInt();
        }

        System.out.println("Enter the size of the files :-");
        for (int i = 1; i <= nf; i++) {
            System.out.print("File " + i + ": ");
            f[i] = scanner.nextInt();
        }

        int lastAllocatedIndex = 1; 

        for (int i = 1; i <= nf; i++) {
            boolean allocated = false;

            for (int j = 0; j < nb; j++) {
                int index = (lastAllocatedIndex + j - 1) % nb + 1; 
                if (!bf[index]) { 
                    if (b[index] >= f[i]) { 
                        ff[i] = index;
                        bf[index] = true; 
                        frag[i] = b[index] - f[i]; 
                        lastAllocatedIndex = index; 
                        allocated = true;
                        break;
                    }
                }
            }

            if (!allocated) { 
                ff[i] = -1; 
                frag[i] = -1; 
            }
        }

        System.out.println("\nFile_no:\tFile_size:\tBlock_no:\tBlock_size:\tFragmentation");
        for (int i = 1; i <= nf; i++) {
            if (ff[i] != -1) {
                System.out.printf("%d\t\t%d\t\t%d\t\t%d\t\t%d%n", i, f[i], ff[i], b[ff[i]], frag[i]);
            } else {
                System.out.printf("%d\t\t%d\t\t-\t\t-\t\t-\n", i, f[i]);
            }
        }

        scanner.close();
    }
}

