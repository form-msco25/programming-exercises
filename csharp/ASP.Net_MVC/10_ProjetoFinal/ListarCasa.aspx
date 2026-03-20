<%@ Page Title="Listar Casas" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ListarCasa.aspx.cs" Inherits="Ex10_ProjetoFinal.ListarCasa" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Lista de Casas</h2>
        <% Lista_dados(); %>
    </main>
</asp:Content>
