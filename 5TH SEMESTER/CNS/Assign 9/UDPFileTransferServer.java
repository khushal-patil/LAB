import java.io.*;
import java.net.*;

public class UDPFileTransferServer {
    private static final int BUFFER_SIZE = 4096; // Size of each UDP packet buffer

    public static void main(String[] args) {
        DatagramSocket socket = null;
        FileOutputStream fileOutput = null;

        try {
            // Create a socket to listen on port 9876
            socket = new DatagramSocket(9876);
            System.out.println("Server is listening on port 9876...");

            // Buffer for receiving data
            byte[] buffer = new byte[BUFFER_SIZE];

            // Receive the file name first
            DatagramPacket fileNamePacket = new DatagramPacket(buffer, buffer.length);
            socket.receive(fileNamePacket);
            String fileName = new String(fileNamePacket.getData(), 0, fileNamePacket.getLength());
            System.out.println("Receiving file: " + fileName);

            // Create file output stream to save the file
            fileOutput = new FileOutputStream("received_" + fileName);

            // Receive the file data
            while (true) {
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet);

                // Check for termination signal (empty packet)
                if (packet.getLength() == 0) {
                    System.out.println("File transfer complete.");
                    break;
                }

                // Write received data to the file
                fileOutput.write(packet.getData(), 0, packet.getLength());
            }

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (fileOutput != null) {
                    fileOutput.close();
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
