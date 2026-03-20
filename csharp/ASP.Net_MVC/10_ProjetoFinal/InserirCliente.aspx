<%@ Page Title="Inserir Cliente" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="InserirCliente.aspx.cs" Inherits="Ex10_ProjetoFinal.InserirCliente" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Inserir Cliente</h2>
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
        
        <asp:Button ID="btn_inserirCliente" runat="server" Text="Inserir Cliente" OnClick="btn_inserirCliente_Click" />
    </main>
</asp:Content>
