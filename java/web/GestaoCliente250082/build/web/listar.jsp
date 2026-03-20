<%-- 
    Document   : listar
    Created on : 16/01/2026, 16:30:08
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
            <h2>Listagem de Clientes</h2>
            <article>
                <table style="border: 1px solid black;">
                    <tr> <!-- linha de cabeçalho -->
                        <th>ID</th>
                        <th>Nome</th> <!-- table header -->
                        <th>Morada</th>
                        <th>Zona</th>
                        <th>NIF</th>                    
                        <th>Volume de faturação</th>
                    </tr><!-- fim da linha de cabeçalho -->
                    <%
                    int num = 0;
                    float media = 0;
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
                    %>
                    <tr>
                        <td><%= rs.getInt("id") %></td>
                        <td><%= rs.getString("nome") %></td>
                        <td><%= rs.getString("morada") %></td>
                        <td><%= rs.getString("zona") %></td>
                        <td><%= rs.getString("nif") %></td>
                        <td><%= rs.getFloat("vol_fatur") %></td>
                    </tr>
                    <%
                            num ++;
                            media = media + rs.getFloat("vol_fatur");
                        }//fim ciclo while
                    %>
                    <tr>
                        <th colspan="5">Total de registos</th>
                        <th><%= num%></th>
                    </tr>
                    <tr>
                        <th colspan="5">Média dos Volumes de Faturação</th>
                        <th><%= media/num %></th>
                    </tr>
                    <%
                    } catch(Exception e){
                        out.println("Ocorreu um erro " + e);
                    }
                    %>
                </table>
            </article>
        </section>        
    </body>
</html>
