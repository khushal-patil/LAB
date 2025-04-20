package com.login.action;

import com.opensymphony.xwork2.ActionSupport;
import com.login.util.DatabaseUtil;
import java.sql.*;

public class LoginAction extends ActionSupport {
    private String email;
    private String password;

    @Override
    public String execute() {
        Connection conn = null;
        try {
            conn = DatabaseUtil.getConnection();
            PreparedStatement ps = conn.prepareStatement(
                "SELECT * FROM students WHERE email = ? AND password = ?");
            ps.setString(1, email);
            ps.setString(2, password);
            
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                return SUCCESS;
            }
            addFieldError("email", "Invalid credentials");
            return INPUT;
        } catch (SQLException e) {
            e.printStackTrace();
            return ERROR;
        } finally {
            DatabaseUtil.closeConnection(conn);
        }
    }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
}