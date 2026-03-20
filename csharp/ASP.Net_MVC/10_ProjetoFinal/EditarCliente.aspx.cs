using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex10_ProjetoFinal
{
    public partial class EditarCliente : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Page_Init(object sender, EventArgs e)
        {
            txt_id.Text = Request.QueryString["id"];
            string connectionString;
            SqlConnection con;
            connectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex10_ProjetoFinal\App_Data\DB_10.mdf;Integrated Security=True";
            con = new SqlConnection(connectionString);
            con.Open();            
            SqlCommand command;
            SqlDataReader dataReader;
            String sql, x;
            sql = "SELECT * FROM Cliente WHERE id=" + Request.QueryString["id"];
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            dataReader.Read();

            txt_id.Text = dataReader.GetValue(0).ToString();
            txt_nome.Text = dataReader.GetValue(1).ToString();
            txt_morada.Text = dataReader.GetValue(2).ToString();
            txt_telefone.Text = dataReader.GetValue(3).ToString();

            dataReader.Close();

            con.Close();
        }

        protected void btn_editarCliente_Click(object sender, EventArgs e)
        {
            string connectionString;
            SqlConnection con;
            connectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex10_ProjetoFinal\App_Data\DB_10.mdf;Integrated Security=True";
            con = new SqlConnection(connectionString);
            con.Open();
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "";
            sql = "UPDATE Cliente set nome = '" + txt_nome.Text + "', morada = '" + txt_morada.Text +
                "', telefone = '" + txt_telefone.Text + "' WHERE id = " + txt_id.Text;
            command = new SqlCommand(sql, con);
            adapter.InsertCommand = new SqlCommand(sql, con);
            adapter.InsertCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
            "alert('Dados alterados com sucesso');window.location = 'GerirCliente.aspx'; ", true);
        }
    }
}