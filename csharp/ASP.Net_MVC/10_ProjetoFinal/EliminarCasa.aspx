<%@ Page Title="Eliminar Casa" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="EliminarCasa.aspx.cs" Inherits="Ex10_ProjetoFinal.EliminarCasa" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Eliminar Casa</h2>
        <br /><br />
        <asp:Label ID="lbl_id" runat="server" Text="ID: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_id" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_zona" runat="server" Text="Zona: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_zona" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_numAssoalhadas" runat="server" Text="Número Assoalhadas: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_numAssoalhadas" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_ano" runat="server" Text="Ano: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_ano" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_preco" runat="server" Text="Preço: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_preco" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        
        <asp:Label ID="lbl_cliente" runat="server" Text="Cliente: "></asp:Label>
        &nbsp;<asp:DropDownList ID="dd_cliente" Enabled="false" runat="server"></asp:DropDownList>
        <br /><br />

        <asp:Button ID="btn_eliminarCasa" runat="server" Text="Eliminar Casa" OnClick="btn_eliminarCasa_Click" />
    </main>
</asp:Content>
