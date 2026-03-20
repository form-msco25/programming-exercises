<%@ Page Title="Listar Clientes" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="ListarCliente.aspx.cs" Inherits="Ex10_ProjetoFinal.ListarCliente" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <main aria-labelledby="title">
        <h2 id="title">Lista de Clientes</h2>
        <% Lista_dados(); %>
    </main>
</asp:Content>
