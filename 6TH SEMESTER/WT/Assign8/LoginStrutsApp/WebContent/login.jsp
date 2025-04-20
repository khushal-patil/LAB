<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="s" uri="/struts-tags" %>
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h2>Student Login</h2>
        <s:form action="login">
            <s:textfield name="email" label="Email"/>
            <s:password name="password" label="Password"/>
            <s:submit value="Login" class="button"/>
        </s:form>
        <p>New user? <a href="register.jsp">Register here</a></p>
    </div>
</body>
</html>