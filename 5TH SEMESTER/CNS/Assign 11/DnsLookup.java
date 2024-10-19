import java.net.*;
import java.util.Scanner;

public class DnsLookup {

    // Method to perform reverse DNS lookup by IP address
    public static String lookupByIp(String ip) {
        try {
            InetAddress inetAddress = InetAddress.getByName(ip);
            return inetAddress.getHostName(); // Return the hostname
        } catch (UnknownHostException e) {
            return "Reverse lookup failed.";
        }
    }

    // Method to perform DNS lookup by hostname
    public static String lookupByHostname(String hostname) {
        try {
            InetAddress inetAddress = InetAddress.getByName(hostname);
            return inetAddress.getHostAddress(); // Return the IP address
        } catch (UnknownHostException e) {
            return "Invalid hostname.";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an IP address or URL: ");
        String input = scanner.nextLine();

        try {
            // Try parsing the input as an IP address first
            InetAddress address = InetAddress.getByName(input);

            // If the input is an IP, perform reverse DNS lookup
            if (address instanceof Inet4Address || address instanceof Inet6Address) {
                String hostname = lookupByIp(input);
                System.out.println("IP Address: " + input + " -> URL: " + hostname);
            } else {
                // If input is not an IP address, treat it as a hostname
                String ip = lookupByHostname(input);
                System.out.println("URL: " + input + " -> IP Address: " + ip);
            }
        } catch (UnknownHostException e) {
            // If the input couldn't be resolved as an IP, treat it as a hostname
            String ip = lookupByHostname(input);
            System.out.println("URL: " + input + " -> IP Address: " + ip);
        }

        scanner.close(); // Close the scanner
    }
}
