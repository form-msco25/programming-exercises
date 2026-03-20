using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex10_ProjetoFinal
{
    public partial class ListarCliente : Page
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
            sql = "SELECT * FROM Cliente";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                Output = Output + 
                    dataReader.GetValue(0) + " - " +
                    dataReader.GetValue(1) + " - " + 
                    dataReader.GetValue(2) + " - " +
                    dataReader.GetValue(3) + "</br>";
            }
            Response.Write(Output);
            dataReader.Close();
            con.Close();
        }
    }
}