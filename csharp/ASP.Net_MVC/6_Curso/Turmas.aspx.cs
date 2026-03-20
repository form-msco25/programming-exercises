using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex6
{
    public partial class Turmas : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Obter_Dados()
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
            String sql, Output = "<table border='1'>";
            Output = Output + "<tr><th>ID</th><th>Turma</th>";            
            Output = Output + "<th>Ação</th></tr>";
            sql = "SELECT * FROM t_turma";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                Output = Output + "<tr><td>" + dataReader.GetValue(0) + "</td>"
                    + "<td>" + dataReader.GetValue(1) + "</td>"                    
                    + "<td><a href='EliminarT.aspx?id=" +
                    dataReader.GetValue(0) + "' target='_self'>Eliminar</a></td></tr>";
            }
            Output = Output + "</table>";
            Response.Write(Output);
            dataReader.Close();
            con.Close();
        }

        protected void btn_inserirTurma_Click(object sender, EventArgs e)
        {
            string connetionString;
            SqlConnection con;
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex6\App_Data\bd_06.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "";
            sql = "INSERT INTO t_turma(turma) values ('" + txt_turma.Text + "')";
            command = new SqlCommand(sql, con);
            adapter.InsertCommand = new SqlCommand(sql, con);
            adapter.InsertCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
            "alert('Turma inserida com sucesso');window.location = 'Turmas.aspx'; ", true);
        }
    }
}