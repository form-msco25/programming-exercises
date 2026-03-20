<%-- 
    Document   : listarTip
    Created on : 06/02/2026, 16:46:02
    Author     : michael
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Gestão Stand - IEFP</title>
        <link href="estilo.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <header>
            <h1>TudoBarato</h1>
        </header>               
        <section>
            <h2>Listagem de Tipos</h2>
            <article>
                <table style="border: 1px solid black;">
                    <tr> <!-- linha de cabeçalho -->
                        <th>ID</th><!-- table header -->
                        <th>Tipo</th>                         
                    </tr><!-- fim da linha de cabeçalho -->
                    <%
                    int num = 0;                    
                    try{
                        //criar a instância da classe a ser usada
                        Class.forName("com.mysql.jdbc.Driver");
                        //criação da conexão à base de dados
                        Connection conn = DriverManager.getConnection(""
                        + "jdbc:mysql://localhost:3306/bd_stand", "root", 
                        "");
                        Statement stmt = conn.createStatement();
                        //defino a instrução a ser executada
                        ResultSet rs = stmt.executeQuery("SELECT * "
                        + "from t_Tipo");
                        //enquanto houver registo faz o ciclo
                        while(rs.next()){
                    %>
                    <tr>
                        <td><%= rs.getInt("id") %></td>
                        <td><%= rs.getString("tipo") %></td>                        
                    </tr>
                    <%
                            num ++;                            
                        }//fim ciclo while
                    %>
                    <tr>
                        <th>Total de registos</th>
                        <th><%= num %></th>          
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