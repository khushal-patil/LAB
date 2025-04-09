import java.io.*;
import java.net.*;

public class CalculatorServer {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12347)) {
            System.out.println("Calculator Server is listening on port 12347");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Client connected");

                new CalculatorHandler(socket).start();
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}

class CalculatorHandler extends Thread {
    private Socket socket;

    public CalculatorHandler(Socket socket) {
        this.socket = socket;
    }

    public void run() {
        try (BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter output = new PrintWriter(socket.getOutputStream(), true)) {

            String clientInput;
            while ((clientInput = input.readLine()) != null) {
                String[] parts = clientInput.split(" ");
                double num1 = Double.parseDouble(parts[0]);
                String operator = parts[1];
                double num2 = Double.parseDouble(parts[2]);
                double result = 0;

                switch (operator) {
                    case "+":
                        result = num1 + num2;
                        break;
                    case "-":
                        result = num1 - num2;
                        break;
                    case "*":
                        result = num1 * num2;
                        break;
                    case "/":
                        if (num2 != 0) {
                            result = num1 / num2;
                        } else {
                            output.println("Error: Division by zero");
                            continue;
                        }
                        break;
                    default:
                        output.println("Error: Invalid operator");
                        continue;
                }

                output.println("Result: " + result);
            }

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
