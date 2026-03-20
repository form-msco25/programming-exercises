using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Ex4
{
    public partial class Inserir : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            
        }

        protected void btn_inserir_Click(object sender, EventArgs e)
        {
            string connetionString;
            SqlConnection con;            
            connetionString = @"Data Source=(LocalDB)\MSSQLLocalDB;
                AttachDbFilename=C:\Users\micha\source\repos\Ex4\App_Data\bd_4.mdf;
                Integrated Security=True";
            con = new SqlConnection(connetionString);
            con.Open();
            SqlCommand command;
            SqlDataAdapter adapter = new SqlDataAdapter();
            String sql = "";
            sql = "INSERT INTO livros(nome, n_paginas, tamanho) values ('" + 
                txt_nome.Text + "', " + txt_npag.Text + ", '" + txt_tam.Text + "')";
            command = new SqlCommand(sql, con);
            adapter.InsertCommand = new SqlCommand(sql, con);
            adapter.InsertCommand.ExecuteNonQuery();
            command.Dispose();
            con.Close();
            ScriptManager.RegisterStartupScript(this, this.GetType(), "Dados",
            "alert('Dados inseridos com sucesso');window.location = 'Lista_Simples.aspx'; ", true);
        }
    }
}