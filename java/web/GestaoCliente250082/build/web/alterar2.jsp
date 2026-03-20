<%-- 
    Document   : alterar2
    Created on : 19/01/2026, 15:05:39
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
                <%
                try{
                    int id = Integer.parseInt(request.getParameter("id"));
                    //criar a instância da classe a ser usada
                    Class.forName("com.mysql.jdbc.Driver");
                    //criação da conexão à base de dados
                    Connection conn = DriverManager.getConnection(""
                    + "jdbc:mysql://localhost:3306/bd_01", "root", "");
                    PreparedStatement pstm = conn.prepareStatement(""
                    + "SELECT * from t_cliente WHERE id = ?");
                    //substituo o ? pelo id que foi mandado por post
                    pstm.setInt(1, id);
                    ResultSet rs = pstm.executeQuery();                    
                    if (rs.next()){
                        %>
                        <form action="alterar3.jsp" method="post">
                            Id:<input type="text" size="10" maxlength="10" readonly 
                                      name="id" value="<%= rs.getInt("id")%>"><br>
                            Nome:<input type="text" size="60" maxlength="100" required
                                        name="nome" value="<%= rs.getString("nome")%>"><br>
                            Morada:<input type="text" size="60" maxlength="100" required
                                          name="morada" 
                                          value="<%= rs.getString("morada")%>"><br>
                            Zona:<input type="text" size="50" maxlength="50" required 
                                        name="zona" value="<%= rs.getString("zona")%>"><br>
                            NIF:<input type="text" size="20" maxlength="9" required
                                       name="nif" value="<%= rs.getString("nif")%>"><br>
                            Volume de faturação:<input type="text" size="10" required
                                                       maxlength="10" name="vol_fatur" 
                                                       value="<%= rs.getFloat("vol_fatur")%>"><br>
                            <input type="submit" value="Alterar">
                        </form>
                        <%                        
                    }                    
                } catch(Exception e){
                    out.println("Ocorreu um erro " + e);
                }
                %>                
            </article>
        </section>
    </body>
</html>
