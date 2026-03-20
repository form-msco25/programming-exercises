using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex6
{
    public partial class Editar : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Page_Init(object sender, EventArgs e)
        {
            txt_numero.Text = Request.QueryString["id"];
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
                dd_genero.Items.Add(new ListItem((string)dataReader.GetValue(1), x));
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

            sql = "SELECT * FROM t_aluno WHERE numero=" + Request.QueryString["id"];
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            dataReader.Read();
            txt_numero.Text = dataReader.GetValue(0).ToString();
            txt_nome.Text = dataReader.GetValue(1).ToString();
            txt_email.Text = dataReader.GetValue(2).ToString();
            txt_data_nasc.Text = dataReader.GetValue(3).ToString();
            txt_morada.Text = dataReader.GetValue(4).ToString();
            dd_genero.SelectedValue = dataReader.GetValue(5).ToString();
            dd_turma.SelectedValue = dataReader.GetValue(6).ToString();
            dataReader.Close();

            con.Close();
        }

        protected void btn_alterar_Click(object sender, EventArgs e)
        {
            string connetionString;
            SqlConnection con;
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex6\App_Data\bd_06.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "";
            sql = "UPDATE t_aluno set nome = '" + txt_nome.Text + "', email = '" + txt_email.Text +
                "', data_nasc = '" + txt_data_nasc.Text + "', morada = '" + txt_morada.Text + 
                "', genero_id = " + dd_genero.SelectedValue + ", turma_id = " + dd_turma.SelectedValue + 
                " WHERE numero = " + txt_numero.Text;
            command = new SqlCommand(sql, con);
            adapter.InsertCommand = new SqlCommand(sql, con);
            adapter.InsertCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
            "alert('Dados alterados com sucesso');window.location = 'Default.aspx'; ", true);
        }
    }
}