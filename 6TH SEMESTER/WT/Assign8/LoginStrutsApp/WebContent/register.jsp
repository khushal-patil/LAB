<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h2>Student Registration</h2>
        <s:form action="register">
            <s:textfield name="student.name" label="Name"/>
            <s:textfield name="student.email" label="Email"/>
            <s:textfield name="student.mobile" label="Mobile"/>
            <s:password name="student.password" label="Password"/>
            <s:submit value="Register" class="button"/>
        </s:form>
        <p>Already registered? <a href="login.jsp">Login here</a></p>
    </div>
</body>
</html>