import java.io.*;
import java.net.*;

public class HelloClient {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345);
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            output.println("Hello, Server!");
            String response = input.readLine();
            System.out.println("Server says: " + response);

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
