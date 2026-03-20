<%-- 
    Document   : pesqMarc
    Created on : 06/02/2026, 16:36:49
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
                    + "jdbc:mysql://localhost:3306/bd_stand", "root", "");
                    String sql = "DELETE FROM t_Marca WHERE id = ?";                    
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
            // caso vá pesquisar
                String texto = request.getParameter("texto");
                %>
                <h3>Pesquisa de <b><i><u> <%=texto%> </u></i></b> nas marcas</h3>
                <table style="border: 1px solid black;" class="table table-striped">
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Marca</th>
                            <th>Ação</th>
                        </tr>
                    </thead>
                </table>
                <%               
                try{
                    //criar a instância da casse a ser usada
                    Class.forName("com.mysql.jdbc.Driver");
                    //criação da conexão à base de dados
                    Connection conn = DriverManager.getConnection(""
                    + "jdbc:mysql://localhost:3306/bd_stand", "root", "");
                    Statement stm = conn.createStatement();
                    int num = 0;
                    ResultSet rs=stm.executeQuery("SELECT * from t_Marca WHERE "
                    + "marca LIKE '%"+texto+"%'");
                    while(rs.next()){
                    %>
                        <tr>
                            <td><%= rs.getInt("id") %></td>
                            <td><%= rs.getString("marca") %></td>
                            <td>
                                <form action="pesqMarc.jsp" method="post">
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
                        <td colspan="2">Registos da Pesquisa</td>
                        <td style="text-align: right;"><%=num%></td>
                    </tr>
                    <%
                    rs.close();
                    stm.close();
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
            <h2>Listagem de Marcas</h2>
            <article>
                <table style="border: 1px solid black;">
                    <tr> <!-- linha de cabeçalho -->
                        <th>ID</th><!-- table header -->
                        <th>Marca</th>                         
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
                        + "from t_Marca");
                        //enquanto houver registo faz o ciclo
                        while(rs.next()){
                    %>
                    <tr>
                        <td><%= rs.getInt("id") %></td>
                        <td><%= rs.getString("marca") %></td>
                        <td>
                            <form action="pesqMarc.jsp" method="post">
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
                        rs.close();
                        stmt.close();
                        conn.close();
                    } catch(Exception e){
                        out.println("Ocorreu um erro " + e);
                    }
                    %>
                </table>                
            </article>
        </section>
        <!-- código inserir.html -->
        <section>
        <h2>Pesquisa de Marca</h2>
            <article>
                <form action="pesqMarc.jsp" method="post">
                    <input type="hidden" name="acao" value="pesquisar">
                    Valor a pesquisar:<input type="text" size="20" maxlength="20" required
                                name="marca" placeholder="Honda, Smart, Volvo ..."><br>   
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