<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Inserir.aspx.cs" Inherits="Ex4.Inserir" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <h1>Inserçao de Livros</h1>
        <div>
            <asp:Label ID="lbl_nome" runat="server" Text="Nome:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_nome" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_npag" runat="server" Text="Nº de páginas:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_npag" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_tam" runat="server" Text="Tamanho:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_tam" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Button ID="btn_inserir" runat="server" Text="Inserir" OnClick="btn_inserir_Click"/>
            <asp:Button ID="btn_cancelar" runat="server" Text="Cancelar"/>
        </div>
    </form>
</body>
</html>
