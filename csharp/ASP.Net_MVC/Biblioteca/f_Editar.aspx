<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="f_Editar.aspx.cs" Inherits="Biblioteca.f_Editar" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <h1>Listagem de Livros</h1>
        <div>
            <asp:FormView ID="FormView1" runat="server" AllowPaging="True" BackColor="White" BorderColor="#336666" BorderStyle="Double" BorderWidth="3px" CellPadding="4" DataSourceID="SqlDataSource1" GridLines="Horizontal">
                <EditItemTemplate>
                    nome:
                    <asp:TextBox ID="nomeTextBox" runat="server" Text='<%# Bind("nome") %>' />
                    <br />
                    n_paginas:
                    <asp:TextBox ID="n_paginasTextBox" runat="server" Text='<%# Bind("n_paginas") %>' />
                    <br />
                    tamanho:
                    <asp:TextBox ID="tamanhoTextBox" runat="server" Text='<%# Bind("tamanho") %>' />
                    <br />
                    <asp:LinkButton ID="UpdateButton" runat="server" CausesValidation="True" CommandName="Update" Text="Atualizar" />
                    &nbsp;<asp:LinkButton ID="UpdateCancelButton" runat="server" CausesValidation="False" CommandName="Cancel" Text="Cancelar" />
                </EditItemTemplate>
                <EditRowStyle BackColor="#339966" Font-Bold="True" ForeColor="White" />
                <FooterStyle BackColor="White" ForeColor="#333333" />
                <HeaderStyle BackColor="#336666" Font-Bold="True" ForeColor="White" />
                <InsertItemTemplate>
                    nome:
                    <asp:TextBox ID="nomeTextBox" runat="server" Text='<%# Bind("nome") %>' />
                    <br />
                    n_paginas:
                    <asp:TextBox ID="n_paginasTextBox" runat="server" Text='<%# Bind("n_paginas") %>' />
                    <br />
                    tamanho:
                    <asp:TextBox ID="tamanhoTextBox" runat="server" Text='<%# Bind("tamanho") %>' />
                    <br />
                    <asp:LinkButton ID="InsertButton" runat="server" CausesValidation="True" CommandName="Insert" Text="Inserir" />
                    &nbsp;<asp:LinkButton ID="InsertCancelButton" runat="server" CausesValidation="False" CommandName="Cancel" Text="Cancelar" />
                </InsertItemTemplate>
                <ItemTemplate>
                    nome:
                    <asp:Label ID="nomeLabel" runat="server" Text='<%# Bind("nome") %>' />
                    <br />
                    n_paginas:
                    <asp:Label ID="n_paginasLabel" runat="server" Text='<%# Bind("n_paginas") %>' />
                    <br />
                    tamanho:
                    <asp:Label ID="tamanhoLabel" runat="server" Text='<%# Bind("tamanho") %>' />
                    <br />

                </ItemTemplate>
                <PagerStyle BackColor="#336666" ForeColor="White" HorizontalAlign="Center" />
                <RowStyle BackColor="White" ForeColor="#333333" />
            </asp:FormView>
            <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT [nome], [n_paginas], [tamanho] FROM [livros]"></asp:SqlDataSource>
        </div>
    </form>
</body>
</html>
