using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex6
{
    public partial class Gerir : Page
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
            Output = Output + "<tr><th>Número</th><th>Nome</th>";
            Output = Output + "<th>E-mail</th><th>Data Nascimento</th>";
            Output = Output + "<th>Morada</th><th>Género</th>";
            Output = Output + "<th>Turma</th></tr>";
            sql = "SELECT * FROM t_aluno, t_genero, t_turma WHERE t_aluno.genero_id = t_genero.id" +
                " AND t_aluno.turma_id = t_turma.id";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                Output = Output + "<tr><td>" + dataReader.GetValue(0) + "</td>"
                    + "<td>" + dataReader.GetValue(1) + "</td>"
                    + "<td>" + dataReader.GetValue(2) + "</td>"
                    + "<td>" + dataReader.GetValue(3) + "</td>"
                    + "<td>" + dataReader.GetValue(4) + "</td>"
                    + "<td>" + dataReader.GetValue(8) + "</td>"
                    + "<td>" + dataReader.GetValue(10) + "</td>"
                    + "<td><input type='button' value='Editar'" +
                    "onclick=window.open('Editar.aspx?id=" +
                    dataReader.GetValue(0) + "') />" +
                    "&nbsp<input type='button' value='Eliminar'" +
                    "onclick=window.open('Eliminar.aspx?id=" +
                    dataReader.GetValue(0) + "') /></td></tr>";
            }
            Output = Output + "</table>";
            Response.Write(Output);
            dataReader.Close();
            con.Close();
        }
    }
}