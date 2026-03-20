using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex10_ProjetoFinal
{
    public partial class GerirCliente : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Obter_Dados()
        {
            string connetionString;
            SqlConnection con;
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex10_ProjetoFinal\App_Data\DB_10.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();            
            SqlCommand command;
            SqlDataReader dataReader;
            String sql, Output = "<table border='1'>";
            Output = Output + "<tr><th>ID</th><th>Zona</th>";
            Output = Output + "<th>Número Assoalhadas</th><th>Ano</th>";
            Output = Output + "<th>Preço</th><th>Cliente</th>";
            Output = Output + "<th>Ações</th></tr>";
            sql = "SELECT Casa.id, Casa.zona, Casa.numAssoalhadas, Casa.ano, Casa.preco, Cliente.nome " + 
                "FROM Casa JOIN Cliente ON Cliente.id = Casa.id_cliente";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                Output = Output + "<tr>" 
                    + "<td>" + dataReader.GetValue(0) + "</td>"
                    + "<td>" + dataReader.GetValue(1) + "</td>"
                    + "<td>" + dataReader.GetValue(2) + "</td>"
                    + "<td>" + dataReader.GetValue(3) + "</td>"
                    + "<td>" + dataReader.GetValue(4) + "</td>"
                    + "<td>" + dataReader.GetValue(5) + "</td>"
                    
                    + "<td><input type='button' value='Editar'" +
                    "onclick=window.open('EditarCasa.aspx?id=" +
                    dataReader.GetValue(0) + "') />" +
                    "&nbsp<input type='button' value='Eliminar'" +
                    "onclick=window.open('EliminarCasa.aspx?id=" +
                    dataReader.GetValue(0) + "') /></td></tr>";
            }
            Output = Output + "</table>";
            Response.Write(Output);
            dataReader.Close();
            con.Close();
        }
    }
}