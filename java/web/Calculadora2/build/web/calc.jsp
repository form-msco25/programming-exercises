<%-- 
    Document   : calc
    Created on : 12/01/2026, 18:57:21
    Author     : michael
    Function   : calculadora
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Calculadora - MO</title>
    </head>
    <body>
        <h1>Calculadora WEB - MO</h1>
        <%
            Double n1 = Double.parseDouble(request.getParameter("n1"));
            Double n2 = Double.parseDouble(request.getParameter("n2"));
            Double res;
            String op = request.getParameter("op");
            if (op.equals("som"))
                res = n1 + n2;
            else if (op.equals("dif"))
                res = n1 - n2;
            else if (op.equals("mul"))
                res = n1 * n2;
            else
                res = n1 / n2;
            out.print("<h3>A operação entre " + n1 + " e " + n2 + " = " + res +
            "</h3>");
        %>
    </body>
</html>
