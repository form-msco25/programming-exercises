<%-- 
    Document   : apagarViat
    Created on : 06/02/2026, 17:55:50
    Author     : michael
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Gestão Stand</title>
        <link href="estilo.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <header>
            <h1>TudoBarato</h1>
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
        <%
        if (request.getMethod().equals("POST")){
            int id = Integer.parseInt(request.getParameter("id"));
            try{
                //criar a instância da casse a ser usada
                Class.forName("com.mysql.jdbc.Driver");
                //criação da conexão à base de dados
                Connection conn = DriverManager.getConnection(""
                + "jdbc:mysql://localhost:3306/bd_01", "root", "");
                String sql = "DELETE FROM t_cliente WHERE id = ?";                    
                PreparedStatement pstm = conn.prepareStatement(sql);
                //substituo os valores pelos pontos de interrogação
                pstm.setInt(1, id);
                //tenta executar a inserção
                int apagado = pstm.executeUpdate();
                if (apagado>0)
                out.print("<h3>Registo apagado com sucesso!</h3>");
                else
                    out.print("<h3>Ocorreu um erro ao eliminar.</h3>");
                pstm.close();
                conn.close();
            } catch(Exception e){
                out.println("Ocorreu um erro " + e);
            }
        }
        %>
        <form action="eliminarR.jsp" method="post">
            Qual o cliente a apagar:
            <select name="id">       
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
            <input type="submit" value="Apagar">
        </form>
    </body>
</html>