using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex10_ProjetoFinal
{
    public partial class InserirCasa : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Page_Init(object sender, EventArgs e)
        {
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
                dd_cliente.Items.Add(new ListItem((string)dataReader.GetValue(1).ToString(), x));
            }
            dataReader.Close();
            con.Close();
        }

        protected void btn_inserirCasa_Click(object sender, EventArgs e)
        {
            string connectionString;
            SqlConnection con;
            connectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex10_ProjetoFinal\App_Data\DB_10.mdf;Integrated Security=True";
            con = new SqlConnection(connectionString);
            con.Open();
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "";
            sql = "INSERT INTO Casa(zona, ano, numAssoalhadas, preco, id_cliente) values " +
                "('" + txt_zona.Text + "', " + txt_ano.Text + ", " + txt_numAssoalhadas.Text + ", " + txt_preco.Text + ", " + dd_cliente.SelectedValue + ")";
            command = new SqlCommand(sql, con);
            adapter.InsertCommand = new SqlCommand(sql, con);
            adapter.InsertCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
            "alert('Dados inseridos com sucesso');window.location = 'ListarCasa.aspx'; ", true);
        }
    }
}