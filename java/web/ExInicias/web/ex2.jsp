<%-- 
    Document   : ex2
    Created on : 12/01/2026, 17:43:47
    Author     : michael
--%>

<%@page contentType="text/html" import="java.util.Date" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Ex2 - Data - MO</title>
    </head>
    <body>
        <h1>Exemplo de 'output' com cálculo</h1>
        <%
            //Instrução que permite escrever dentro de html
            out.print("<h2>Exemplo de um output</h2>");
            // Cálculo + concatenação
            out.print("A multiplicaçáo de 5 a 2 = " + 5*2);
            out.print("<h3>"+ new Date() + "</h3>");
        %>
    </body>
</html>
