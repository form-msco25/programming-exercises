using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex6
{
    public partial class Listagem : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Lista_dados()
        {
            string connetionString;
            SqlConnection con;
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex6\App_Data\bd_06.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            // Response.Write("Ligado com sucesso!");
            // a linha acima utilizo apenas para ver se a conexão é feita com sucesso
            SqlCommand command;
            SqlDataReader dataReader;
            String sql, Output = " ";
            sql = "SELECT * FROM t_aluno, t_genero, t_turma WHERE t_aluno.genero_id = t_genero.id" + 
                " AND t_aluno.turma_id = t_turma.id";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                Output = Output + dataReader.GetValue(0) + " - " +
                    dataReader.GetValue(1) + " - " + dataReader.GetValue(2) + " - " 
                    + dataReader.GetValue(3) + " - " + dataReader.GetValue(4) + " - "
                    + dataReader.GetValue(8) + " - " + dataReader.GetValue(10) + "</br>";
            }
            Response.Write(Output);
            dataReader.Close();
            con.Close();
        }
    }
}