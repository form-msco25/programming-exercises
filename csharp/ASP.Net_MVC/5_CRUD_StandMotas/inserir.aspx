<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="inserir.aspx.cs" Inherits="Ex5.inserir" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <h1>Inserçao de Motas</h1>
        <div>
            <asp:Label ID="lbl_matricula" runat="server" Text="Matrícula:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_matricula" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_proprietario" runat="server" Text="Proprietario:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_proprietario" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_marca" runat="server" Text="Marca:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_marca" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_modelo" runat="server" Text="Modelo:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_modelo" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Label ID="lbl_cilindrada" runat="server" Text="Cilindrada:"></asp:Label>&nbsp;
            <asp:TextBox ID="txt_cilindrada" runat="server"></asp:TextBox>
            <br /><br />
            <asp:Button ID="btn_inserir" runat="server" Text="Inserir" OnClick="btn_inserir_Click"/>&nbsp
            <asp:Button ID="btn_cancelar" runat="server" Text="Cancelar"/>&nbsp
        </div>
    </form>
</body>
</html>
