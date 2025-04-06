<%@ page import="java.sql.*, db.DBConnection" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Student Info</title>
    <style>
        body {
            font-family: 'Segoe UI';
            background: linear-gradient(to right, #e0eafc, #cfdef3);
            margin: 0;
            padding: 0;
        }

        .container {
            width: 80%;
            margin: 50px auto;
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        h2 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 15px;
            text-align: center;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }
        .error {
            text-align: center;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Student Information</h2>
        <%
            Connection conn = null;
            Statement stmt = null;
            ResultSet rs = null;

            try {
                conn = DBConnection.getConnection();
                stmt = conn.createStatement();
                rs = stmt.executeQuery("SELECT * FROM students_info");
        %>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Class</th>
                <th>Division</th>
                <th>City</th>
            </tr>
            <%
                while(rs.next()) {
            %>
            <tr>
                <td><%= rs.getInt("stud_id") %></td>
                <td><%= rs.getString("stud_name") %></td>
                <td><%= rs.getString("class") %></td>
                <td><%= rs.getString("division") %></td>
                <td><%= rs.getString("city") %></td>
            </tr>
            <% 
                } 
            %>
        </table>
        <%
            } catch(Exception e) {
                e.getMessage();
            } finally {
                try {
                    if(rs != null) rs.close();
                    if(stmt != null) stmt.close();
                    if(conn != null) conn.close();
                } catch(Exception ex) {
                    out.println("Closing Error: " + ex.getMessage());
                }
            }
        %>
    </div>
</body>
</html>
