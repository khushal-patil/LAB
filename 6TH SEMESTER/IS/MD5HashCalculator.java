import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class MD5HashCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter text: ");
        String input = scanner.nextLine();
        scanner.close();

        try {
            // Create a MessageDigest instance for MD5
            MessageDigest md = MessageDigest.getInstance("MD5");

            // Update the digest with the input bytes
            md.update(input.getBytes());

            // Compute the hash
            byte[] digest = md.digest();

            // Convert the hash to a hexadecimal string
            String hash = bytesToHex(digest);

            System.out.println("MD5(\"" + input + "\") = " + hash);
        } catch (NoSuchAlgorithmException e) {
            System.err.println("MD5 algorithm not found.");
        }
    }

    private static String bytesToHex(byte[] bytes) {
        char[] hexDigits = "0123456789ABCDEF".toCharArray();
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            hexString.append(hexDigits[(b >> 4) & 0x0F]);
            hexString.append(hexDigits[b & 0x0F]);
        }
        return hexString.toString().toLowerCase();

    }
}
