package com.example;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/EbookshopServlet")
public class EbookshopServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    public EbookshopServlet() {}
    

    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String url = "jdbc:mysql://localhost:3306/Assign5"; 
        String user = "root";  
        String password = "root@123"; 

        out.println("<html><head><title>Ebookshop</title></head><body>");
        out.println("<h2>Ebookshop Books</h2>");
        out.println("<table border='1'><tr><th>ID</th><th>Title</th><th>Author</th><th>Price</th><th>Qty</th></tr>");

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement stmt = conn.createStatement();
            String selectSql = "SELECT * FROM ebookshop";
            ResultSet rs = stmt.executeQuery(selectSql);

            while (rs.next()) {
                out.println("<tr><td>" + rs.getInt("book_id") + "</td>");
                out.println("<td>" + rs.getString("book_title") + "</td>");
                out.println("<td>" + rs.getString("book_author") + "</td>");
                out.println("<td>" + rs.getDouble("book_price") + "</td>");
                out.println("<td>" + rs.getInt("quantity") + "</td></tr>");
            }

            out.println("</table></body></html>");

            rs.close();
            stmt.close();
            conn.close();
        } catch (ClassNotFoundException e) {
            out.println("<p>Error: MySQL JDBC Driver not found!</p>");
            e.printStackTrace();
        } catch (SQLException e) {
            out.println("<p>Error: Database connection failed!</p>");
            e.printStackTrace();
        }
    }
}
