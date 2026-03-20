using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex10_ProjetoFinal
{
    public partial class EditarCasa : Page
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
            sql = "SELECT * FROM Cliente";
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            while (dataReader.Read())
            {
                x = dataReader.GetValue(0) + "";                
                dd_cliente.Items.Add(new ListItem((string)dataReader.GetValue(1), x));
            }
            dataReader.Close();

            sql = "SELECT * FROM Casa WHERE id=" + Request.QueryString["id"];
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            dataReader.Read();
            txt_id.Text = dataReader.GetValue(0).ToString();
            txt_zona.Text = dataReader.GetValue(1).ToString();
            txt_numAssoalhadas.Text = dataReader.GetValue(2).ToString();
            txt_ano.Text = dataReader.GetValue(3).ToString();
            txt_preco.Text = dataReader.GetValue(4).ToString();
            dd_cliente.SelectedValue = dataReader.GetValue(5).ToString();            
            dataReader.Close();

            con.Close();
        }

        protected void btn_editarCasa_Click(object sender, EventArgs e)
        {
            string connectionString;
            SqlConnection con;
            connectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex10_ProjetoFinal\App_Data\DB_10.mdf;Integrated Security=True";
            con = new SqlConnection(connectionString);
            con.Open();
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "";
            sql = "UPDATE Casa set zona = '" + txt_zona.Text + "', numAssoalhadas = " + txt_numAssoalhadas.Text +
                ", ano = " + txt_ano.Text + ", preco = " + txt_preco.Text +
                ", id_cliente = " + dd_cliente.SelectedValue + " WHERE id = " + txt_id.Text;
            command = new SqlCommand(sql, con);
            adapter.InsertCommand = new SqlCommand(sql, con);
            adapter.InsertCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
            "alert('Dados alterados com sucesso');window.location = 'GerirCasa.aspx'; ", true);
        }
    }
}