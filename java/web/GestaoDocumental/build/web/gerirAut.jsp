<%-- 
    Document   : gerirAut
    Created on : 26/01/2026, 16:04:27
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
        <!-- código inserir.jsp -->
        <%
        // no caso de existir um POST, coloco o código do inserirCat.jsp
        if (request.getMethod().equals("POST")){
            String acao = request.getParameter("acao");
            if (acao.equals("apagar")){
            // caso seja apagar
                int id = Integer.parseInt(request.getParameter("id"));
                try{
                    //criar a instância da casse a ser usada
                    Class.forName("com.mysql.jdbc.Driver");
                    //criação da conexão à base de dados
                    Connection conn = DriverManager.getConnection(""
                    + "jdbc:mysql://localhost:3306/bd_02", "root", "");
                    String sql = "DELETE FROM tAutor WHERE id = ?";                    
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
            }else{            
            // caso vá inserir
                String cat = request.getParameter("nome");
                try{
                    //criar a instância da casse a ser usada
                    Class.forName("com.mysql.jdbc.Driver");
                    //criação da conexão à base de dados
                    Connection conn = DriverManager.getConnection(""
                    + "jdbc:mysql://localhost:3306/bd_02", "root", "");
                    String sql = "INSERT INTO tAutor (nome) VALUES (?)";
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
            // fim do inserir
            }
        }            
        %>
        <!-- código listarCat.jsp -->
        <section>
            <h2>Listagem de Autores</h2>
            <article>
                <table style="border: 1px solid black;">
                    <tr> <!-- linha de cabeçalho -->
                        <th>ID</th><!-- table header -->
                        <th>Nome</th>                         
                    </tr><!-- fim da linha de cabeçalho -->
                    <%
                    int num = 0;                    
                    try{
                        //criar a instância da classe a ser usada
                        Class.forName("com.mysql.jdbc.Driver");
                        //criação da conexão à base de dados
                        Connection conn = DriverManager.getConnection(""
                        + "jdbc:mysql://localhost:3306/bd_02", "root", 
                        "");
                        Statement stmt = conn.createStatement();
                        //defino a instrução a ser executada
                        ResultSet rs = stmt.executeQuery("SELECT * "
                        + "from tAutor");
                        //enquanto houver registo faz o ciclo
                        while(rs.next()){
                    %>
                    <tr>
                        <td><%= rs.getInt("id") %></td>
                        <td><%= rs.getString("nome") %></td>
                        <td>
                            <form action="gerirAut.jsp" method="post">
                                <input type="hidden" name="id" value="<%= rs.getInt("id") %>">
                                <input type="hidden" name="acao" value="apagar">
                                <input type="submit" value="Apagar">
                            </form>
                        </td>
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
        <!-- código inserir.html -->
        <section>
        <h2>Inserção de Autores</h2>
            <article>
                <form action="gerirAut.jsp" method="post">
                    Nome:<input type="text" size="20" maxlength="20" required
                                name="nome" placeholder="Michael Ortiz, Steven Cataño, ..."><br>   
                    <input type="hidden" name="acao" value="inserir">
                    <input type="submit" value="Inserir">
                </form>
            </article>
        </section>
        <footer>
            <h4>Desenvolvido por Michael Ortiz @ IEFP VNG</h4>
        </footer>
    </body>
</html>