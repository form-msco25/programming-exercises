<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Eliminar.aspx.cs" Inherits="Ex4.Eliminar" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <br />
            <asp:Label ID="lbl_id" runat="server" Text="Id:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_id" runat="server" Columns="3" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_nome" runat="server" Text="Nome:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_nome" runat="server" Columns="50" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_npag" runat="server" Text="Nº de páginas:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_npag" runat="server" Columns="5" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_tam" runat="server" Text="Tamanho:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_tam" runat="server" Columns="10" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Button ID="btn_eliminar" runat="server" Text="Apagar" OnClick="btn_eliminar_Click"/>&nbsp;
            <asp:Button ID="btn_cancelar" runat="server" Text="Cancelar"/>
        </div>
    </form>
</body>
</html>
