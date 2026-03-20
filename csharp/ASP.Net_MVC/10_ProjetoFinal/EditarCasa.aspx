<%@ Page Title="Editar Casa" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="EditarCasa.aspx.cs" Inherits="Ex10_ProjetoFinal.EditarCasa" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Editar Casa</h2>
        <br /><br />
        <asp:Label ID="lbl_id" runat="server" Text="ID: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_id" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_zona" runat="server" Text="Zona: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_zona" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_numAssoalhadas" runat="server" Text="Número Assoalhadas: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_numAssoalhadas" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_ano" runat="server" Text="Ano: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_ano" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_preco" runat="server" Text="Preço: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_preco" runat="server"></asp:TextBox>
        <br /><br />
        
        <asp:Label ID="lbl_cliente" runat="server" Text="Cliente: "></asp:Label>
        &nbsp;<asp:DropDownList ID="dd_cliente" runat="server"></asp:DropDownList>        
        <br /><br />
        
        <asp:Button ID="btn_editarCasa" runat="server" Text="Editar Casa" OnClick="btn_editarCasa_Click" />
    </main>
</asp:Content>
