<%-- 
    Document   : gerirViat
    Created on : 06/02/2026, 15:08:07
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
                    String sql = "DELETE FROM t_Viatura WHERE id=?";          
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
                String matricula = request.getParameter("matricula");
                int ano = Integer.parseInt(request.getParameter("ano"));
                int cilindrada = Integer.parseInt(request.getParameter("cilindrada"));
                int kms = Integer.parseInt(request.getParameter("kms"));
                String modelo = request.getParameter("modelo");
                float preco = Float.parseFloat("preco");
                int tipo = Integer.parseInt(request.getParameter("tipo"));
                int marca = Integer.parseInt(request.getParameter("marca"));
                try{
                    //criar a instância da casse a ser usada
                    Class.forName("com.mysql.jdbc.Driver");
                    //criação da conexão à base de dados
                    Connection conn = DriverManager.getConnection(""
                    + "jdbc:mysql://localhost:3306/bd_stand", "root", "");
                    String sql = "INSERT INTO t_Viatura (matricula, ano, cilindrada, " + 
                    "kms, modelo, preco, tipo, marca) " + 
                    "VALUES (?,?,?,?,?,?,?,?)";
                    PreparedStatement pstm = conn.prepareStatement(sql);
                    //substituo os valores pelos pontos de interrogação
                    pstm.setString(1, matricula);
                    pstm.setInt(2, ano);
                    pstm.setInt(3, cilindrada);
                    pstm.setInt(4, kms);
                    pstm.setString(5, modelo);
                    pstm.setFloat(6, preco);
                    pstm.setInt(7, tipo);
                    pstm.setInt(8, marca);    
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
            <h2>Gerir Viaturas</h2>
            <article>
                <table style="border: 1px solid black;">
                    <tr> <!-- linha de cabeçalho -->
                        <th>ID</th><!-- table header -->
                        <th>Matrícula</th>
                        <th>Ano</th>
                        <th>Cilindrada</th>
                        <th>Kms</th>
                        <th>Modelo</th>
                        <th>Preco</th>
                        <th>Marca</th>
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
                        + "from t_Viatura, t_Marca, t_Tipo " + 
                        "WHERE t_Viatura.id_marca = t_Marca.id AND " +
                        "t_Viatura.id_tipo = t_Tipo.id");
                        //enquanto houver registo faz o ciclo
                        while(rs.next()){
                    %>
                    <tr>
                        <td><%= rs.getInt("t_Viatura.id") %></td>
                        <td><%= rs.getString("matricula") %></td>
                        <td><%= rs.getInt("ano") %></td>
                        <td><%= rs.getInt("cilindrada") %></td>
                        <td><%= rs.getInt("kms") %></td>
                        <td><%= rs.getString("modelo") %></td>
                        <td><%= rs.getFloat("preco") %></td>
                        <td><%= rs.getInt("t_Marca.marca") %></td>
                        <td><%= rs.getInt("t_Tipo.tipo") %></td>                        
                        <td>
                            <form action="gerirViat.jsp" method="post">
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
        <h2>Inserção de Viaturas</h2>
            <article>
                <form action="inserirViat.jsp" method="post">
                    Matricula: <input type="text" size="20" maxlength="20" required 
                                 name="matricula"><br>
                    Ano: <input type="text" size="10" maxlength="10" required
                                 name="ano"><br>
                    Cilindrada: <input type="number" size="10" maxlength="10" required
                                 name="cilindrada"><br>
                    Kms: <input type="number" size="20" maxlength="20" 
                                 name="kms"><br>
                    Modelo: <input type="text" size="50" maxlength="50" 
                                 name="modelo"><br>
                    Preco: <input type="number" size="20" maxlength="20" 
                                 name="preco"><br>                    
                    Marca: <select name="marca">
                        <%
                        try{
                            //criar a instância da classe a ser usada
                            Class.forName("com.mysql.jdbc.Driver");
                            //criação da conexão à base de dados
                            Connection conn = DriverManager.getConnection(""
                            + "jdbc:mysql://localhost:3306/bd_stand", "root", 
                            "");
                            Statement stmt = conn.createStatement();
                            //defino a instrução a ser executada
                            ResultSet rs = stmt.executeQuery("SELECT * from " + 
                            "t_Marca");
                            //enquanto houver registo faz o ciclo
                            while(rs.next()){
                                out.print("<option value='"+rs.getInt("id")+"'>");
                                out.print(rs.getString("Marca")+"</option>");                                
                            }
                        }catch (Exception e){
                            out.println("Ocorreu um erro "+e);
                        }
                        %>
                    </select>
                    Tipo: <select name="tipo">
                        <%
                        try{
                            //criar a instância da classe a ser usada
                            Class.forName("com.mysql.jdbc.Driver");
                            //criação da conexão à base de dados
                            Connection conn = DriverManager.getConnection(""
                            + "jdbc:mysql://localhost:3306/bd_stand", "root", 
                            "");
                            Statement stmt = conn.createStatement();
                            //defino a instrução a ser executada
                            ResultSet rs = stmt.executeQuery("SELECT * from " + 
                            "t_Tipo");
                            //enquanto houver registo faz o ciclo
                            while(rs.next()){
                                out.print("<option value='"+rs.getInt("id")+"'>");
                                out.print(rs.getString("Tipo")+"</option>");                                
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