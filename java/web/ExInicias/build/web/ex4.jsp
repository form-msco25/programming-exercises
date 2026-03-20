<%-- 
    Document   : ex4
    Created on : 12/01/2026, 18:23:36
    Author     : michael
--%>

<%@page contentType="text/html"  import="java.lang.String" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Exemplo POST - MO</title>
    </head>
    <body>
        <h1>Bem-vindo ao JSP</h1>
        <%
            String nome = request.getParameter("nome");
            String uNome = request.getParameter("unome");
            out.print("<h3>Olá " + nome + " " + uNome + "!</h3>");
        %>
    </body>
</html>
