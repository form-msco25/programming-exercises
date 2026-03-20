using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex5
{
    public partial class eliminar : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Page_Init(object sender, EventArgs e)
        {
            txt_id.Text = Request.QueryString["id"];
            string connetionString;
            SqlConnection con;            
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex5\App_Data\bd_5.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            // Response.Write("Ligado com sucesso!");
            // a linha acima utilizo apenas para ver se a conexão é feita com sucesso
            SqlCommand command;
            SqlDataReader dataReader;
            String sql;
            sql = "SELECT * FROM motas where id=" + Request.QueryString["id"];
            command = new SqlCommand(sql, con);
            dataReader = command.ExecuteReader();
            dataReader.Read();
            //carregar os dados para dentro do form
            txt_matricula.Text = dataReader.GetValue(1).ToString();
            txt_proprietario.Text = dataReader.GetValue(2).ToString();
            txt_marca.Text = dataReader.GetValue(3).ToString();
            txt_modelo.Text = dataReader.GetValue(4).ToString();
            txt_cilindrada.Text = dataReader.GetValue(5).ToString();
        }

        protected void btn_eliminar_Click(object sender, EventArgs e)
        {
            string connetionString;
            SqlConnection con;
            // veja a imagem abaixo para saber onde vai buscar o caminho da conexão
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\micha\source\repos\Ex5\App_Data\bd_5.mdf;Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            // Response.Write("Ligado com sucesso!");
            // a linha acima utilizo apenas para ver se a conexão é feita com sucesso
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "DELETE motas where Id=" + txt_id.Text;
            // Response.Write(sql);
            // a linha acima serve para verem o que esta a ser executado no vosso sql
            command = new SqlCommand(sql, con);
            adapter.DeleteCommand = new SqlCommand(sql, con);
            adapter.DeleteCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
           "alert('Registo apagado com sucesso');window.location='Listar.aspx';", true);
        }
    }
}