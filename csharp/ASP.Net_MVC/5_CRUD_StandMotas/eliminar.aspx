<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="eliminar.aspx.cs" Inherits="Ex5.eliminar" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <h1>Eliminação de Motas</h1>
    <form id="form1" runat="server">
        <div>
            <br />
            <asp:Label ID="lbl_id" runat="server" Text="Id:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_id" runat="server" Columns="3" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_matricula" runat="server" Text="Matrícula:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_matricula" runat="server" Columns="50" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_proprietario" runat="server" Text="Prorietario:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_proprietario" runat="server" Columns="5" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_marca" runat="server" Text="Marca:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_marca" runat="server" Columns="10" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_modelo" runat="server" Text="Modelo:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_modelo" runat="server" Columns="10" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_cilindrada" runat="server" Text="Cilindrada:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_cilindrada" runat="server" Columns="10" ReadOnly="true"></asp:TextBox>
            <br /><br />
            <asp:Button ID="btn_eliminar" runat="server" Text="Apagar" OnClick="btn_eliminar_Click"/>&nbsp;
            <asp:Button ID="btn_cancelar" runat="server" Text="Cancelar"/>
        </div>
    </form>
</body>
</html>
