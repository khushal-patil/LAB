import java.io.*;
import java.net.*;

public class CalculatorClient {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12347);
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            String expression;

            System.out.println("Enter calculations in the format 'num1 operator num2' (e.g., '3 + 4'): ");
            while ((expression = userInput.readLine()) != null) {
                output.println(expression);
                String response = input.readLine();
                System.out.println(response);
            }

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
