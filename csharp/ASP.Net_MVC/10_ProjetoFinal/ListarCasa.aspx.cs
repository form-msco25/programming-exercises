using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex10_ProjetoFinal
{
    public partial class ListarCasa : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Lista_dados()
        {
            string connectionString;
            SqlConnection con;
            connectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex10_ProjetoFinal\App_Data\DB_10.mdf;Integrated Security=True";
            con = new SqlConnection(connectionString);
            con.Open();            
            SqlCommand command;
            SqlDataReader dataReader;
            String sql, Output = "";
            sql = "SELECT Cliente.nome, Casa.zona, Casa.numAssoalhadas, Casa.ano, Casa.preco " +
                  "FROM Casa JOIN Cliente ON Cliente.id = Casa.id_cliente";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                Output = Output + 
                    dataReader.GetValue(0) + " - " +
                    dataReader.GetValue(1) + " - " + 
                    dataReader.GetValue(2) + " - " +
                    dataReader.GetValue(3) + " - " + 
                    dataReader.GetValue(4) + "</br>";
            }
            Response.Write(Output);
            dataReader.Close();
            con.Close();
        }
    }
}