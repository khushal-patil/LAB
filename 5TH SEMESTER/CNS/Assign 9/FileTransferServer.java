import java.io.*;
import java.net.*;

public class FileTransferServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12346)) {
            System.out.println("File Transfer Server is listening on port 12346");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Client connected");

                new FileTransferHandler(socket).start();
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}

class FileTransferHandler extends Thread {
    private Socket socket;

    public FileTransferHandler(Socket socket) {
        this.socket = socket;
    }

    public void run() {
        try (DataInputStream input = new DataInputStream(socket.getInputStream());
                FileOutputStream fileOutput = new FileOutputStream("received_file.txt")) {

            int bytesRead;
            byte[] buffer = new byte[4096];

            while ((bytesRead = input.read(buffer)) != -1) {
                fileOutput.write(buffer, 0, bytesRead);
            }

            System.out.println("File received!");

        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            try {
                socket.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }
}
