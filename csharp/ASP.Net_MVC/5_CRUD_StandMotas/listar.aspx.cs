using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex5
{
    public partial class listar : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string connetionString;
            SqlConnection con;            
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex5\App_Data\bd_5.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            // Response.Write("Ligado com sucesso!");
            // a linha acima utilizo apenas para ver se a conexão é feita com sucesso
            SqlCommand command;
            SqlDataReader dataReader;
            String sql, Output = " ";
            sql = "SELECT id, matricula, proprietario, marca, modelo, cilindrada FROM motas";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                Output = Output + dataReader.GetValue(0) + " - " +
                    dataReader.GetValue(1) + " - " + dataReader.GetValue(2) + " - " + 
                    dataReader.GetValue(3) + " - " + dataReader.GetValue(4) + " - " + 
                    dataReader.GetValue(5) + "</br>";
            }
            Response.Write(Output);
            dataReader.Close();
            con.Close();
        }
    }
}