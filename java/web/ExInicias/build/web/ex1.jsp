<%-- 
    Document   : ex1
    Created on : 12/01/2026, 17:29:47
    Author     : michael
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Ex1 - Calc - MO</title>
    </head>
    <body>
        <h1>Exemplo de 'output' com cálculo</h1>
        <%
            //Instrução que permite escrever dentro de html
            out.print("<h2>Exemplo de um output</h2>");
            // Cálculo + concatenação
            out.print("A multiplicaçáo de 5 a 2 = " + 5*2);
        %>
    </body>
</html>
