<%@ page isErrorPage="true" %>
<html>
<head><title>Error</title></head>
<body>
    <h2>Oops! Something went wrong.</h2>
    <p>We encountered an unexpected error. Please try again later.</p>
    <p><b>Error Details:</b> <%= exception.getMessage() %></p>
</body>
</html>
