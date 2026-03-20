using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex6
{
    public partial class Inserir : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Page_Init(object sender, EventArgs e)
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
            String sql, x;
            sql = "SELECT * FROM t_genero";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                x = dataReader.GetValue(0) + "";
                // ao adicionar o item no dropdown o 1º, é o valor que é mostrado
                // o 2º o valor do objeeto
                dd_genero.Items.Add(new ListItem((string)dataReader.GetValue(1),x));
            }            
            dataReader.Close();

            sql = "SELECT * FROM t_turma";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                x = dataReader.GetValue(0) + "";
                // ao adicionar o item no dropdown o 1º, é o valor que é mostrado
                // o 2º o valor do objeeto
                dd_turma.Items.Add(new ListItem((string)dataReader.GetValue(1), x));
            }
            dataReader.Close();

            con.Close();
        }

        protected void btn_inserir_Click(object sender, EventArgs e)
        {
            string connetionString;
            SqlConnection con;
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex6\App_Data\bd_06.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "";
            sql = "INSERT INTO t_aluno(nome, email, data_nasc, morada, genero_id, turma_id) values " +
                "('" + txt_nome.Text + "', '" + txt_email.Text + "', '" + txt_data_nasc.Text + "', '" + txt_morada.Text + "', " + dd_genero.SelectedValue + ", " + dd_turma.SelectedValue + ")";
            command = new SqlCommand(sql, con);
            adapter.InsertCommand = new SqlCommand(sql, con);
            adapter.InsertCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
            "alert('Dados inseridos com sucesso');window.location = 'Listagem.aspx'; ", true);
        }
    }
}