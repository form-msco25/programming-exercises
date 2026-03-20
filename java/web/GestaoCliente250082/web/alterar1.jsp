<%-- 
    Document   : alterar1
    Created on : 19/01/2026, 14:48:24
    Author     : michael
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Gestão de Clientes - MO</title>
        <link href="estilo.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <header>
            <h1>Gestão de Clientes - MO</h1>
        </header>
        <nav>
            <a href="index.jsp">Menu Principal</a>
            <a href="listar.jsp">Listar</a>
            <a href="inserir.html">Inserir</a>
            <a href="inserirR.jsp">InserirR</a>
            <a href="eliminar1.jsp">Eliminar</a>
            <a href="eliminarR.jsp">EliminarR</a>           
            <a href="alterar1.jsp">Alterar</a>
        </nav>
        <section>
            <h2>Alteração de Clientes</h2>
            <article>
                <form action="alterar2.jsp" method="post">
                    Qual o cliente a alterar:
                    <select>name="id">
                    <%
                    try{
                        //criar a instância da classe a ser usada
                        Class.forName("com.mysql.jdbc.Driver");
                        //criação da conexão à base de dados
                        Connection conn = DriverManager.getConnection(""
                        + "jdbc:mysql://localhost:3306/bd_01", "root", 
                        "");
                        Statement stmt = conn.createStatement();
                        //defino a instrução a ser executada
                        ResultSet rs = stmt.executeQuery("SELECT * "
                        + "from t_cliente");
                        //enquanto houver registo faz o ciclo
                        while(rs.next()){
                            out.print("<option value='" + rs.getInt("id")+"'>"+
                                rs.getString("nome") + "</option>");                      
                        }//fim ciclo while                   
                    } catch(Exception erro){
                        out.println("Ocorreu um erro " + erro);
                    }
                    %>                
                    </select><br>
                    <input type="submit" value="Alterar">
                </form>
            </article>
        </section>
    </body>
</html>
