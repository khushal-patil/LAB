import java.io.*;
import java.net.*;

public class FileTransferClient {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12346);
                FileInputStream fileInput = new FileInputStream("file_to_send.txt");
                DataOutputStream output = new DataOutputStream(socket.getOutputStream())) {

            byte[] buffer = new byte[4096];
            int bytesRead;

            while ((bytesRead = fileInput.read(buffer)) != -1) {
                output.write(buffer, 0, bytesRead);
            }

            System.out.println("File sent!");

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
