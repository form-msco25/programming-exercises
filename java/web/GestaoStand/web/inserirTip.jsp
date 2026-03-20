<%-- 
    Document   : inserirTip
    Created on : 06/02/2026, 16:49:58
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
        <% 
        if (request.getMethod().equals("POST")){
            String tip = request.getParameter("tipo");
            try{
                //criar a instância da casse a ser usada
                Class.forName("com.mysql.jdbc.Driver");
                //criação da conexão à base de dados
                Connection conn = DriverManager.getConnection(""
                + "jdbc:mysql://localhost:3306/bd_stand", "root", "");
                String sql = "INSERT INTO t_Tipo (tipo) VALUES (?)";
                PreparedStatement pstm = conn.prepareStatement(sql);
                //substituo os valores pelos pontos de interrogação
                pstm.setString(1, tip);             
                //tenta executar a inserção
                int inserido = pstm.executeUpdate();
                if (inserido>0)
                out.print("<h3>Registo inserido com sucesso!</h3>");
                else
                    out.print("<h3>Ocorreu um erro na inserção.</h3>");
                pstm.close();
                conn.close();
            } catch(Exception e){
                out.println("Ocorreu um erro " + e);
            }        
        }            
        %>
        <section>
        <h2>Inserção de Tipos</h2>
            <article>
                <form action="inserirTip.jsp" method="post">
                    Tipo:<input type="text" size="20" maxlength="20" required
                                name="tipo" placeholder="Gasolina, Gasóleo, Híbrido ..."><br>                    
                    <input type="submit" value="Inserir">
                </form>
            </article>
        </section>                   
    </body>
</html>