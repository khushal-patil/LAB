import java.io.*;

class Hello {
    public static void main(String[] args) throws IOException {
        int n = 5;
        // DataInputStream d = new DataInputStream(System.in);
        // System.out.println("Enter a Number: ");
        // n = Integer.parseInt(d.readLine());

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < i; j++) {

                System.out.print(" *");
            }
            System.out.println();
        }
        System.out.println("\n\n");
        for (int i = 0; i <= n; i++) {
            for (int j = i; j <= n - 1; j++) {
                System.out.print(" *");
            }
            System.out.println("");
        }
    }
}
