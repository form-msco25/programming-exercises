<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="index.aspx.cs" Inherits="Ex5.index" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Stand Motas</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <img width="250" src="~/pics/cb125r.jpg" alt="Honda CB125R" runat="server"/><br /><br />
            <asp:Button id="btn_listar" runat="server" Text="Listar" OnClick="btn_listar_Click"/>&nbsp;
            <asp:Button id="btn_inserir" runat="server" Text="Inserir" OnClick="btn_inserir_Click" />&nbsp;            
            <asp:Button id="btn_alterar" runat="server" Text="Alterar/Eliminar" OnClick="btn_alterar_Click" />&nbsp;
        </div>
    </form>
</body>
</html>