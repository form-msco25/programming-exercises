<%-- 
    Document   : gerirDocs
    Created on : 26/01/2026, 17:14:36
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
                    String sql = "DELETE FROM tDocumento WHERE id=?";          
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
                int autor = Integer.parseInt(request.getParameter("autor"));
                int idsubcat = Integer.parseInt(request.getParameter("idsubcat"));
                int publico = Integer.parseInt(request.getParameter("publico"));
                String nome = request.getParameter("nome");
                String isbn = request.getParameter("isbn");
                String descricao = request.getParameter("descricao");
                String tamanho = request.getParameter("tamanho");
                String foto = request.getParameter("foto");
                String ficheiro = request.getParameter("ficheiro");
                try{
                    //criar a instância da casse a ser usada
                    Class.forName("com.mysql.jdbc.Driver");
                    //criação da conexão à base de dados
                    Connection conn = DriverManager.getConnection(""
                    + "jdbc:mysql://localhost:3306/bd_02", "root", "");
                    String sql = "INSERT INTO tDocumento (nome, isbn, descricao, " + 
                    "tamanho, foto, ficheiro, subcat, publico, autor)" + 
                    "VALUES (?,?,?,?,?,?,?,?,?)";
                    PreparedStatement pstm = conn.prepareStatement(sql);
                    //substituo os valores pelos pontos de interrogação
                    pstm.setString(1, nome);
                    pstm.setString(2, isbn);
                    pstm.setString(3, descricao);
                    pstm.setString(4, tamanho);
                    pstm.setString(5, foto);
                    pstm.setString(6, ficheiro);
                    pstm.setInt(7, autor);
                    pstm.setInt(8, idsubcat);
                    pstm.setInt(9, publico);
                    
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
            <h2>Gerir Documentos</h2>
            <article>
                <table style="border: 1px solid black;">
                    <tr> <!-- linha de cabeçalho -->
                        <th>ID</th><!-- table header -->
                        <th>Nome</th>
                        <th>ISBN</th>
                        <th>Descrição</th>
                        <th>Tamanho</th>
                        <th>Foto</th>
                        <th>Ficheiro</th>
                        <th>Subcategoria</th>
                        <th>Público</th>
                        <th>Privado</th>
                        <th>Ficheiro</th>
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
                        + "from tDocumento, tSubCategoria, tAutor" + 
                        "WHERE tDocumento.idSubCat = tSubCategoria.id AND" +
                        "tDocumento.autor = tAutor.id");
                        //enquanto houver registo faz o ciclo
                        while(rs.next()){
                    %>
                    <tr>
                        <td><%= rs.getInt("tDocumento.id") %></td>
                        <td><%= rs.getString("tDocumento.nome") %></td>
                        <td><%= rs.getString("isbn") %></td>
                        <td><%= rs.getString("descricao") %></td>
                        <td><%= rs.getString("tamanho") %></td>
                        <td><img width="100" src="<%= rs.getString("foto")%>"></td>
                        <td><a href="<%= rs.getString("ficheiro")%>">Download</a></td>"
                        <td><%= rs.getString("tSubCategoria.subCategoria") %></td>
                        <td><%= rs.getInt("publico") %></td>
                        <td>
                            <form action="gerirDocs.jsp" method="post">
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
        <h2>Inserção de Documentos</h2>
            <article>
                <form action="gerirDocs.jsp" method="post">
                    Nome: <input type="text" size="50" maxlength="50" required 
                                 name="nome"><br>
                    ISBN: <input type="text" size="20" maxlength="20" 
                                 name="isbn"><br>
                    Descrição: <br><textarea type="text" size="20" maxlength="20" 
                                              name="foto"></textarea><br>
                    Tamanho: <input type="text" size="20" maxlength="20"
                                name="tamanho"><br>
                    Ficheiro (url): <br><textarea name="ficheiro"></textarea></br>
                    Subcategoria: <select name="idsubcat">
                        <%
                        try{
                            //criar a instância da classe a ser usada
                            Class.forName("com.mysql.jdbc.Driver");
                            //criação da conexão à base de dados
                            Connection conn = DriverManager.getConnection(""
                            + "jdbc:mysql://localhost:3306/bd_02", "root", 
                            "");
                            Statement stmt = conn.createStatement();
                            //defino a instrução a ser executada
                            ResultSet rs = stmt.executeQuery("SELECT * from" + 
                            "tSubCategoria");
                            //enquanto houver registo faz o ciclo
                            while(rs.next()){
                                out.print("<option value='"+rs.getInt("id")+"'>");
                                out.print(rs.getString("Subcategoria")+"</option>");                                
                            }
                        }catch (Exception e){
                            out.println("Ocorreu um erro "+e);
                        }
                        %>
                    </select>
                    Público: <select name="publico">
                        <option value="0">Público</option>
                        <option value="1">Privado</option>
                    </select>
                    Autor: <select name="autor">
                        <%
                        try{
                            //criar a instância da classe a ser usada
                            Class.forName("com.mysql.jdbc.Driver");
                            //criação da conexão à base de dados
                            Connection conn = DriverManager.getConnection(""
                            + "jdbc:mysql://localhost:3306/bd_02", "root", 
                            "");
                            Statement stmt = conn.createStatement();
                            //defino a instrução a ser executada
                            ResultSet rs = stmt.executeQuery("SELECT * from" + 
                            "tAutor");
                            //enquanto houver registo faz o ciclo
                            while(rs.next()){
                                out.print("<option value='"+rs.getInt("id")+"'>");
                                out.print(rs.getString("Nome")+"</option>");                                
                            }
                        }catch (Exception e){
                            out.println("Ocorreu um erro "+e);
                        }
                        %>
                    </select>
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