<%-- 
    Document   : ex3
    Created on : 12/01/2026, 17:51:19
    Author     : michael
--%>

<%@page contentType="text/html" import="java.lang.String" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Uso de String</title>
    </head>
    <body>
        <h1>Exemplo de Output de uma String</h1>
        <%
            String nome = "Michael Ortiz";
            out.print("<h2>Bem-vindo " + nome + " ao JSP!</h2>");
        %>
    </body>
</html>
