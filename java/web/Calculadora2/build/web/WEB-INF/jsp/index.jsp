<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Calculadora - MO</title>
    </head>

    <body>
        <h1>Calculadora Web</h1>
        <form action="index.jsp" method="post">
            Qual o número 1: <input type="text" name="n1"><br>
            Qual o número 2: <input type="text" name="n2"><br>
            Qual a operação:<br>
            <input type="radio" name="op" value="som" checked>Soma<br>
            <input type="radio" name="op" value="dif">Diferença<br>
            <input type="radio" name="op" value="mul">Multiplicação<br>
            <input type="radio" name="op" value="div">Divisão<br>
            <input type="submit" value="Calcular">
            <input type="reset" value="Limpar">
        </form>
        <%
            if (request.getMethod().equals("POST")){
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
            }
        %>
    </body>
</html>
