<%-- 
    Document   : inserir
    Created on : 16/01/2026, 18:21:40
    Author     : michael
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Gestão de Cliente - MO</title>
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
            <h2>Inserção de Clientes</h2>
            <article>
                <%
                String nome = request.getParameter("nome");
                String morada = request.getParameter("morada");
                String zona = request.getParameter("zona");
                String nif = request.getParameter("nif");
                String vol_fatur = request.getParameter("vol_fatur");
                try{
                    //criar a instância da casse a ser usada
                    Class.forName("com.mysql.jdbc.Driver");
                    //criação da conexão à base de dados
                    Connection conn = DriverManager.getConnection(""
                    + "jdbc:mysql://localhost:3306/bd_01", "root", "");
                    String sql = "INSERT INTO t_cliente (nome, morada, zona,"
                    + "nif, vol_fatur) VALUES (?,?,?,?,?)";
                    PreparedStatement pstm = conn.prepareStatement(sql);
                    //substituo os valores pelos pontos de interrogação
                    pstm.setString(1, nome);
                    pstm.setString(2, morada);
                    pstm.setString(3, zona);
                    pstm.setString(4, nif);
                    pstm.setString(5, vol_fatur);
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
                %>
            </article>
        </section>
    </body>
</html>
