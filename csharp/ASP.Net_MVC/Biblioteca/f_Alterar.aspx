<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="f_Alterar.aspx.cs" Inherits="Biblioteca.f_Alterar" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <h1>Editar / Alterar / Inserir Utilizadores</h1>
        <div>
            <asp:FormView ID="FormView1" runat="server" AllowPaging="True" BackColor="White" BorderColor="#336666" BorderStyle="Double" BorderWidth="3px" CellPadding="4" DataKeyNames="Id" DataSourceID="SqlDataSource1" GridLines="Horizontal">
                <EditItemTemplate>
                    Id:
                    <asp:Label ID="IdLabel1" runat="server" Text='<%# Eval("Id") %>' />
                    <br />
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
                    Id:
                    <asp:Label ID="IdLabel" runat="server" Text='<%# Eval("Id") %>' />
                    <br />
                    nome:
                    <asp:Label ID="nomeLabel" runat="server" Text='<%# Bind("nome") %>' />
                    <br />
                    n_paginas:
                    <asp:Label ID="n_paginasLabel" runat="server" Text='<%# Bind("n_paginas") %>' />
                    <br />
                    tamanho:
                    <asp:Label ID="tamanhoLabel" runat="server" Text='<%# Bind("tamanho") %>' />
                    <br />
                    <asp:LinkButton ID="EditButton" runat="server" CausesValidation="False" CommandName="Edit" Text="Editar" />
                    &nbsp;<asp:LinkButton ID="DeleteButton" runat="server" CausesValidation="False" CommandName="Delete" Text="Excluir" />
                    &nbsp;<asp:LinkButton ID="NewButton" runat="server" CausesValidation="False" CommandName="New" Text="Novo" />
                </ItemTemplate>
                <PagerStyle BackColor="#336666" ForeColor="White" HorizontalAlign="Center" />
                <RowStyle BackColor="White" ForeColor="#333333" />
            </asp:FormView>
            <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConflictDetection="CompareAllValues" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" DeleteCommand="DELETE FROM [livros] WHERE [Id] = @original_Id AND (([nome] = @original_nome) OR ([nome] IS NULL AND @original_nome IS NULL)) AND (([n_paginas] = @original_n_paginas) OR ([n_paginas] IS NULL AND @original_n_paginas IS NULL)) AND (([tamanho] = @original_tamanho) OR ([tamanho] IS NULL AND @original_tamanho IS NULL))" InsertCommand="INSERT INTO [livros] ([nome], [n_paginas], [tamanho]) VALUES (@nome, @n_paginas, @tamanho)" OldValuesParameterFormatString="original_{0}" SelectCommand="SELECT * FROM [livros]" UpdateCommand="UPDATE [livros] SET [nome] = @nome, [n_paginas] = @n_paginas, [tamanho] = @tamanho WHERE [Id] = @original_Id AND (([nome] = @original_nome) OR ([nome] IS NULL AND @original_nome IS NULL)) AND (([n_paginas] = @original_n_paginas) OR ([n_paginas] IS NULL AND @original_n_paginas IS NULL)) AND (([tamanho] = @original_tamanho) OR ([tamanho] IS NULL AND @original_tamanho IS NULL))">
                <DeleteParameters>
                    <asp:Parameter Name="original_Id" Type="Int32" />
                    <asp:Parameter Name="original_nome" Type="String" />
                    <asp:Parameter Name="original_n_paginas" Type="Int32" />
                    <asp:Parameter Name="original_tamanho" Type="String" />
                </DeleteParameters>
                <InsertParameters>
                    <asp:Parameter Name="nome" Type="String" />
                    <asp:Parameter Name="n_paginas" Type="Int32" />
                    <asp:Parameter Name="tamanho" Type="String" />
                </InsertParameters>
                <UpdateParameters>
                    <asp:Parameter Name="nome" Type="String" />
                    <asp:Parameter Name="n_paginas" Type="Int32" />
                    <asp:Parameter Name="tamanho" Type="String" />
                    <asp:Parameter Name="original_Id" Type="Int32" />
                    <asp:Parameter Name="original_nome" Type="String" />
                    <asp:Parameter Name="original_n_paginas" Type="Int32" />
                    <asp:Parameter Name="original_tamanho" Type="String" />
                </UpdateParameters>
            </asp:SqlDataSource>
        </div>
    </form>
</body>
</html>
