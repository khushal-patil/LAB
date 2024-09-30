import java.util.Scanner;

class Subnet {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input IP Address
        System.out.println("Enter the IP address: ");
        String ip = sc.nextLine();

        // Split the IP address based on '.'
        String split_ip[] = ip.split("\\.");
        String split_bip[] = new String[4];
        String bip = "";

        // Convert IP to binary
        System.out.println("IP Address in binary is:");
        for (int i = 0; i < 4; i++) {
            split_bip[i] = appendZeros(Integer.toBinaryString(Integer.parseInt(split_ip[i])));
            System.out.print(split_bip[i] + " ");
            bip += split_bip[i];
        }
        System.out.println();

        // Input number of addresses
        System.out.print("Enter the number of addresses: ");
        int n = sc.nextInt();

        // Calculate number of bits required and subnet mask
        int bits = (int) Math.ceil(Math.log(n) / Math.log(2));
        System.out.println("Number of bits required for addresses: " + bits);
        int mask = 32 - bits;
        System.out.println("Subnet Mask: " + mask);

        // Create Subnet address
        int fbip[] = new int[32];
        for (int i = 0; i < 32; i++) {
            fbip[i] = (int) bip.charAt(i) - 48; // Convert binary string to int
        }

        for (int i = 31; i > 31 - bits; i--) {
            fbip[i] &= 0; // Set the host bits to 0
        }

        String fip[] = { "", "", "", "" };
        for (int i = 0; i < 32; i++) {
            fip[i / 8] += fbip[i]; // Append the binary bits to form the subnet IP
        }

        System.out.print("Subnet Address: ");
        for (int i = 0; i < 4; i++) {
            System.out.print(Integer.parseInt(fip[i], 2)); // Convert binary to decimal
            if (i != 3)
                System.out.print(".");
        }
        System.out.println();

        // Create Broadcast address
        int lbip[] = new int[32];
        for (int i = 0; i < 32; i++) {
            lbip[i] = (int) bip.charAt(i) - 48;
        }

        for (int i = 31; i > 31 - bits; i--) {
            lbip[i] |= 1; // Set the host bits to 1
        }

        String lip[] = { "", "", "", "" };
        for (int i = 0; i < 32; i++) {
            lip[i / 8] += lbip[i]; // Append the binary bits to form the broadcast IP
        }

        System.out.print("Broadcast Address: ");
        for (int i = 0; i < 4; i++) {
            System.out.print(Integer.parseInt(lip[i], 2)); // Convert binary to decimal
            if (i != 3)
                System.out.print(".");
        }
        System.out.println();
    }

    // Helper function to append leading zeros to a binary string
    static String appendZeros(String s) {
        String temp = "00000000";
        return temp.substring(s.length()) + s;
    }
}
