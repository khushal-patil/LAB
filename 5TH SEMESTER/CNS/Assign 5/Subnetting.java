import java.util.Scanner;

class Subnetting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input IP Address
        System.out.println("Enter the IP address (e.g., 192.168.4.10): ");
        String ip = sc.nextLine();

        // Input CIDR bits
        System.out.println("Enter CIDR notation (e.g., /26): ");
        int cidr = sc.nextInt();

        // Split the IP address into octets
        String[] split_ip = ip.split("\\.");
        String[] split_bip = new String[4];
        String bip = "";

        // Convert IP to binary
        System.out.println("IP Address in binary:");
        for (int i = 0; i < 4; i++) {
            split_bip[i] = appendZeros(Integer.toBinaryString(Integer.parseInt(split_ip[i])));
            System.out.print(split_bip[i] + " ");
            bip += split_bip[i];
        }
        System.out.println();

        // Calculate number of bits required for subnetting
        int bits = 32 - cidr;
        int total_hosts = (int) Math.pow(2, bits);
        System.out.println("Total number of addresses per subnet: " + total_hosts);

        // Calculate subnet mask
        int[] subnet_mask = calculateSubnetMask(cidr);
        System.out.print("Subnet Mask: ");
        for (int i = 0; i < 4; i++) {
            System.out.print(subnet_mask[i]);
            if (i != 3)
                System.out.print(".");
        }
        System.out.println();

        // Calculate subnet address
        System.out.print("Subnet Address: ");
        printAddress(bip, bits, false);

        // Calculate broadcast address
        System.out.print("Broadcast Address: ");
        printAddress(bip, bits, true);

        // Number of subnets to create
        System.out.print("Enter the number of subnets to form: ");
        int subnetCount = sc.nextInt();
        createSubnets(bip, bits, total_hosts, subnetCount);

        sc.close();
    }

    // Helper function to append leading zeros to a binary string
    static String appendZeros(String s) {
        String temp = "00000000";
        return temp.substring(s.length()) + s;
    }

    // Helper function to calculate the subnet mask
    static int[] calculateSubnetMask(int cidr) {
        int[] subnet_mask = new int[4];
        for (int i = 0; i < cidr / 8; i++) {
            subnet_mask[i] = 255;
        }
        if (cidr % 8 != 0) {
            subnet_mask[cidr / 8] = 256 - (int) Math.pow(2, 8 - cidr % 8);
        }
        return subnet_mask;
    }

    // Helper function to print the subnet or broadcast address
    static void printAddress(String bip, int bits, boolean isBroadcast) {
        int[] addressBits = new int[32];
        for (int i = 0; i < 32; i++) {
            addressBits[i] = (int) bip.charAt(i) - 48;
        }

        for (int i = 31; i > 31 - bits; i--) {
            if (isBroadcast) {
                addressBits[i] |= 1; // Set the host bits to 1 for broadcast
            } else {
                addressBits[i] &= 0; // Set the host bits to 0 for subnet
            }
        }

        // Convert the 32-bit binary address to decimal format and print
        String[] address = { "", "", "", "" };
        for (int i = 0; i < 32; i++) {
            address[i / 8] += addressBits[i];
        }

        for (int i = 0; i < 4; i++) {
            System.out.print(Integer.parseInt(address[i], 2));
            if (i != 3)
                System.out.print(".");
        }
        System.out.println();
    }

    // Helper function to create subnets
    static void createSubnets(String bip, int bits, int total_hosts, int subnetCount) {
        int baseIncrement = total_hosts;

        for (int j = 1; j < subnetCount; j++) {
            // Calculate and print first address of each subnet
            System.out.print("Subnet " + (j + 1) + " First Address: ");
            printSubnetAddress(bip, bits, j * baseIncrement, false);

            // Calculate and print last address of each subnet
            System.out.print("Subnet " + (j + 1) + " Last Address: ");
            printSubnetAddress(bip, bits, j * baseIncrement, true);
        }
    }

    // Helper function to print the first and last addresses of subnets
    static void printSubnetAddress(String bip, int bits, int increment, boolean isLast) {
        int[] addressBits = new int[32];
        for (int i = 0; i < 32; i++) {
            addressBits[i] = (int) bip.charAt(i) - 48;
        }

        for (int i = 31; i > 31 - bits; i--) {
            if (isLast) {
                addressBits[i] |= 1; // Set the host bits to 1 for last address
            } else {
                addressBits[i] &= 0; // Set the host bits to 0 for first address
            }
        }

        // Convert binary to decimal and add subnet increment
        String[] address = { "", "", "", "" };
        for (int i = 0; i < 32; i++) {
            address[i / 8] += addressBits[i];
        }

        for (int i = 0; i < 4; i++) {
            int decimalValue = Integer.parseInt(address[i], 2);
            if (i == 3)
                decimalValue += increment; // Add increment to last octet
            System.out.print(decimalValue);
            if (i != 3)
                System.out.print(".");
        }
        System.out.println();
    }
}
