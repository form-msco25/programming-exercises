<%@ Page Title="Generos" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Generos.aspx.cs" Inherits="Ex6.Generos" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Gerir Géneros</h2>
        <% Obter_Dados(); %>
        <br /><br />
        <h3>Adicionar Género</h3>
        <asp:Label ID="lbl_genero" runat="server" Text="Género: "></asp:Label>
        &nbsp;<asp:TextBox ID="txt_genero" runat="server"></asp:TextBox>
        <br /><br />
        <asp:Button ID="btn_inserirGenero" runat="server" Text="Inserir Género" OnClick="btn_inserirGenero_Click" />
    </main>
</asp:Content>