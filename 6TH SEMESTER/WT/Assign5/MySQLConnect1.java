import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MySQLConnect1 {
    public static void main(String[] args) {
        // Database URL, username, and password
        String url = "jdbc:mysql://localhost:3306/Assign5"; // Replace with your database name
        String user = "root";  // Replace with your MySQL username
        String password = "root@123";  // Replace with your MySQL password

        try {
            // Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish the connection
            Connection conn = DriverManager.getConnection(url, user, password);
            System.out.println("Connected to the database successfully!");

            // Create a Statement
            Statement stmt = conn.createStatement();

            // Update book price and quantity where book_id = 1
            String updateSql = "UPDATE ebookshop SET book_price = 39.99, quantity = 15 WHERE book_id = 1";
            int rowsUpdated = stmt.executeUpdate(updateSql);
            if (rowsUpdated > 0) {
                System.out.println("Book details updated successfully.");
            }

            // Execute SQL Query to retrieve all records from the ebookshop table
            String selectSql = "SELECT * FROM ebookshop"; // Adjust the table name if needed
            ResultSet rs = stmt.executeQuery(selectSql);

            // Print column headers
            System.out.println("\n=== Ebookshop Table ===");
            System.out.printf("%-5s %-30s %-20s %-10s %-10s%n", "ID", "Title", "Author", "Price", "Qty");
            System.out.println("-------------------------------------------------------------");

            // Iterate through the result set and print the records
            while (rs.next()) {
                int id = rs.getInt("book_id");
                String title = rs.getString("book_title");
                String author = rs.getString("book_author");
                double price = rs.getDouble("book_price");
                int qty = rs.getInt("quantity");

                System.out.printf("%-5d %-30s %-20s %-10.2f %-10d%n", id, title, author, price, qty);
            }

            // Close the resources
            rs.close();
            stmt.close();
            conn.close();
        } catch (ClassNotFoundException e) {
            System.out.println("MySQL JDBC Driver not found!");
            e.printStackTrace();
        } catch (SQLException e) {
            System.out.println("Connection failed!");
            e.printStackTrace();
        }
    }
}
