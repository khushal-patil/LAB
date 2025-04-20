package com.login.action;

import com.opensymphony.xwork2.ActionSupport;
import com.login.model.Student;
import com.login.util.DatabaseUtil;
import java.sql.*;

public class RegisterAction extends ActionSupport {
    private Student student = new Student();

    @Override
    public String execute() {
        Connection conn = null;
        try {
            conn = DatabaseUtil.getConnection();
            PreparedStatement ps = conn.prepareStatement(
                "INSERT INTO students (name, email, mobile, password) VALUES (?, ?, ?, ?)");
            ps.setString(1, student.getName());
            ps.setString(2, student.getEmail());
            ps.setString(3, student.getMobile());
            ps.setString(4, student.getPassword());
            
            int result = ps.executeUpdate();
            if (result > 0) {
                return SUCCESS;
            }
            return INPUT;
        } catch (SQLException e) {
            e.printStackTrace();
            return ERROR;
        } finally {
            DatabaseUtil.closeConnection(conn);
        }
    }

    @Override
    public void validate() {
        if (student.getName() == null || student.getName().trim().isEmpty()) {
            addFieldError("student.name", "Name is required");
        }
        if (student.getEmail() == null || student.getEmail().trim().isEmpty()) {
            addFieldError("student.email", "Email is required");
        }
        if (student.getMobile() == null || student.getMobile().trim().isEmpty()) {
            addFieldError("student.mobile", "Mobile number is required");
        }
        if (student.getPassword() == null || student.getPassword().trim().isEmpty()) {
            addFieldError("student.password", "Password is required");
        }
    }

    public Student getStudent() { return student; }
    public void setStudent(Student student) { this.student = student; }
}