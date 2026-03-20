<%@ Page Title="Editar Cliente" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="EditarCliente.aspx.cs" Inherits="Ex10_ProjetoFinal.EditarCliente" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Editar Cliente</h2>
        <br /><br />
        <asp:Label ID="lbl_id" runat="server" Text="ID: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_id" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_nome" runat="server" Text="Nome: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_nome" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_morada" runat="server" Text="Morada: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_morada" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_telefone" runat="server" Text="Telefone: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_telefone" runat="server"></asp:TextBox>
        <br /><br />        
        
        <asp:Button ID="btn_editarCliente" runat="server" Text="Editar Cliente" OnClick="btn_editarCliente_Click" />
    </main>
</asp:Content>
