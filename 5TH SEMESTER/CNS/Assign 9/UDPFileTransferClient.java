import java.io.*;
import java.net.*;

public class UDPFileTransferClient {
    private static final int BUFFER_SIZE = 4096; // Size of each UDP packet buffer

    public static void main(String[] args) {
        DatagramSocket socket = null;
        FileInputStream fileInput = null;

        try {
            // Specify the file to send
            File file = new File("file_to_send.txt"); // Change this to the file path of your text/audio/video/script
            String serverAddress = "localhost"; // Change this to the server IP address if on different machines
            int serverPort = 9876;

            // Create a UDP socket
            socket = new DatagramSocket();
            InetAddress serverInetAddress = InetAddress.getByName(serverAddress);

            // Send the file name first
            byte[] fileNameBytes = file.getName().getBytes();
            DatagramPacket fileNamePacket = new DatagramPacket(fileNameBytes, fileNameBytes.length, serverInetAddress,
                    serverPort);
            socket.send(fileNamePacket);

            // Read the file and send its content in packets
            fileInput = new FileInputStream(file);
            byte[] buffer = new byte[BUFFER_SIZE];
            int bytesRead;

            while ((bytesRead = fileInput.read(buffer)) != -1) {
                DatagramPacket packet = new DatagramPacket(buffer, bytesRead, serverInetAddress, serverPort);
                socket.send(packet);
            }

            // Send an empty packet to indicate the end of file transfer
            DatagramPacket endPacket = new DatagramPacket(new byte[0], 0, serverInetAddress, serverPort);
            socket.send(endPacket);

            System.out.println("File sent successfully!");

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (fileInput != null) {
                    fileInput.close();
                }
                if (socket != null) {
                    socket.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
