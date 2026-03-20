<%@ Page Title="Eliminar Cliente" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="EliminarCliente.aspx.cs" Inherits="Ex10_ProjetoFinal.EliminarCliente" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Eliminar Cliente</h2>
        <br /><br />
        <asp:Label ID="lbl_id" runat="server" Text="ID: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_id" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_nome" runat="server" Text="Nome: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_nome" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_morada" runat="server" Text="Morada: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_morada" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Label ID="lbl_telefone" runat="server" Text="Telefone: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_telefone" ReadOnly="true" runat="server"></asp:TextBox>
        <br /><br />
        

        <asp:Button ID="btn_eliminarCliente" runat="server" Text="Eliminar Cliente" OnClick="btn_eliminarCliente_Click" />
    </main>
</asp:Content>
