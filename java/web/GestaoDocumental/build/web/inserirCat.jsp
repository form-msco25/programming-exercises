<%-- 
    Document   : inserirCat
    Created on : 23/01/2026, 16:54:00
    Author     : michael
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Gestão Documental - IEFP</title>
    </head>
    <body>
        <header>
            <h1>Gestão Documental - IEFP</h1>
        </header>        
        <% 
        if (request.getMethod().equals("POST")){
            String cat = request.getParameter("categoria");
            try{
                //criar a instância da casse a ser usada
                Class.forName("com.mysql.jdbc.Driver");
                //criação da conexão à base de dados
                Connection conn = DriverManager.getConnection(""
                + "jdbc:mysql://localhost:3306/bd_02", "root", "");
                String sql = "INSERT INTO tCategoria (categoria) VALUES (?)";
                PreparedStatement pstm = conn.prepareStatement(sql);
                //substituo os valores pelos pontos de interrogação
                pstm.setString(1, cat);             
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
        <h2>Inserção de Categorias</h2>
            <article>
                <form action="inserirCat.jsp" method="post">
                    Categoria:<input type="text" size="20" maxlength="20" required
                                name="categoria" placeholder="Romanco, técnico, ..."><br>                    
                    <input type="submit" value="Inserir">
                </form>
            </article>
        </section>                   
    </body>
</html>